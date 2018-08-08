# coding: utf-8

'''

Codes between the '*' are data structures which are used for getting the precision recall and f score

'''


import pandas as pd
import json
import re
from itertools import combinations


class SituationClustering(object):
    def __init__(self, input_path, output_path):
        self.KB = {}
        self.input_path = input_path
        self.output_path = output_path

        # for test
        self.ground_truth = {}
        self.ground_truth_pair = []
        self.clustering_labels_pair = []
        self.clustering_labels = {}
        self.data_labeled = pd.DataFrame()
        self.mark = []
        self.id = []
        self.gpe = []
        self.label = []
        self.data_labeled_gpe = pd.DataFrame()
    #
    @staticmethod
    def remove_plus(text):
        text = text.strip('[')
        text = text.strip(']')
        text = re.sub("\n+", " ", text)
        text = re.sub("#", "", text)
        pattern = re.compile(r'@\w+')
        text = re.sub(pattern, '', text)
        pattern = re.compile(r'[0-9][a-zA-z]+://[^\s]*')
        text = re.sub(pattern, '', text)
        text = re.sub("u'", "", text)
        text = re.sub('u"', "", text)
        text = re.sub(";", "", text)
        text = re.sub(",", "", text)
        text = re.sub("'", "", text)
        text = re.sub('"', "", text)
        text = re.sub("'s", "", text)
        text = re.sub("&", "", text)
        text = ''.join(i for i in text if not i.isdigit())
        text = re.sub("-", "", text)
        text = text.strip()
        return text
    #

    @staticmethod
    def read_json(line):
        """
        Reading json data line by line (streaming)
        :param line:
        :return: dictionary format of data
        """
        return json.loads(line)

    def update_kb_gpe(self, dic):
        """
        Updating the clustering data structure
        :param dic:
        :return: updated dic
        """
        #
        if dic['mark'] not in self.ground_truth:
            self.ground_truth[dic['mark']] = []
            self.ground_truth[dic['mark']].append(dic['id'])
        else:
            self.ground_truth[dic['mark']].append(dic['id'])
        #

        key = self.remove_plus(dic['GPE'].encode('utf-8').lower())
        if key not in self.KB:
            self.KB[key] = []
            self.KB[key].append(dic['id'])
        else:
            self.KB[key].append(dic['id'])
        #
        self.gpe.append(key)
        self.mark.append(dic['mark'])
        self.id.append(dic['id'])
        #

    def kb_to_situation_clustering(self):
        """
        Transferring global dictionary(i.e clustering data structure) to a json-line file
        :output: .txt file
        """
        f = open(self.output_path, 'wb')
        num = 1

        id_label = {}

        for k,v in self.KB.items():
            result = {}
            result['cluster'+str(num)] = v
            result['preferred_name'] = k
            f.write(json.dumps(result))
            f.write('\n')
            #
            for each in v:
                id_label[each] = num
            #
            num += 1

        #
        self.data_labeled['id'] = self.id
        self.data_labeled['mark'] = self.mark
        self.data_labeled['gpe'] = self.gpe
        label = []
        for row in self.data_labeled.iterrows():
            label.append(id_label[row[1]['id']])
        self.data_labeled['gpe_graph'] = label
        for i in range(self.data_labeled .shape[0]):
            if self.data_labeled['mark'].iloc[i] == 0:
                self.data_labeled['mark'].iloc[i] = None
        self.data_labeled = self.data_labeled.reset_index(drop=True)
        self.data_labeled_gpe = self.data_labeled.dropna(axis=0, how='any')
        #

    def run(self):
        """
        The main function, including three frames: read_json, update_kb, kb_to_situation_clustering
        """
        f = open(self.input_path, 'r')
        while True:
            line = f.readline()
            if line:
                dic = self.read_json(line)
                self.update_kb_gpe(dic)
            else:
                break
        f.close()
        self.kb_to_situation_clustering()

    def analysis_result(self):
        """
        Computing the presion, recall, f-score of the situation clustering algorithm
        """
        self.ground_truth.pop(0)
        for k, v in self.ground_truth.items():
            self.ground_truth_pair = self.ground_truth_pair + list(combinations(sorted(v), 2))

        # Compute clustering labels and pairs
        print '==clustering (GPE)=='
        print 'Number Precision  Recall  F1 score'
        for row in self.data_labeled_gpe.iterrows():
            if row[1]['gpe_graph'] in self.clustering_labels.keys():
                self.clustering_labels[row[1]['gpe_graph']].append(row[1]['id'])
            else:
                self.clustering_labels[row[1]['gpe_graph']] = []
                self.clustering_labels[row[1]['gpe_graph']].append(row[1]['id'])
        for k, v in self.clustering_labels.items():
            self.clustering_labels_pair = self.clustering_labels_pair + list(combinations(sorted(v), 2))

        TP = len(list(set(self.ground_truth_pair).intersection(set(self.clustering_labels_pair))))
        FP = len(list(set(self.clustering_labels_pair).difference(set(self.ground_truth_pair))))
        FN = len(list(set(self.ground_truth_pair).difference(set(self.clustering_labels_pair))))
        pre = float(TP) / (TP + FP)
        recall = float(TP) / (TP + FN)
        f_score = 2.0 * pre * recall / (pre + recall)
        print round(pre, 5), round(recall, 5), round(f_score, 5)


SC = SituationClustering('test_streaming.txt', 'clustering_result.txt')
SC.run()
SC.analysis_result()