# coding: utf-8

'''

Codes between the '*' are data structures which are used for getting the precision recall and f score

'''

import json


class LocationTopics(object):
    def __init__(self,output_path):
        try:
            self.f = open(output_path, 'wb')
        except IOError:
            print "Error: Please enter the right format of output file."
        else:
            self.KB = {}
            self.id_text = {}
            # for checkpoint
            self.checkpoint_step = 1000
            self.checkpoint = 0

    def update_kb(self, dic):
        """
        Updating the clustering data structure
        :param dic:
        :return: updated dic
        """
        # the rule to cluster doc
        self.id_text[dic['id']] = dic['text_original']
        if dic['GPE'] is not None:
            for each_gpe in dic['GPE']:
                each_gpe = each_gpe.encode('utf-8').lower()
                if dic['topics']:
                    for each_topic in dic['topics']:
                        each_topic = each_topic.encode('utf-8').lower()
                        key = each_gpe + ' : '+each_topic
                        if key not in self.KB:
                            self.KB[key] = []
                            self.KB[key].append(dic['id'])
                        else:
                            self.KB[key].append(dic['id'])
                else:
                    if dic['Annotation'] is not None:
                        key = each_gpe + ' : ' + dic['Annotation']['Type']
                        if each_gpe not in self.KB:
                            self.KB[key] = []
                            self.KB[key].append(dic['id'])
                        else:
                            self.KB[key].append(dic['id'])
                    else:
                        key = each_gpe + ' : '+'without topics'
                        if each_gpe not in self.KB:
                            self.KB[key] = []
                            self.KB[key].append(dic['id'])
                        else:
                            self.KB[key].append(dic['id'])
        else:
            if dic['LOC'] is not None:
                for each_loc in dic['LOC']:
                    each_loc = each_loc.encode('utf-8').lower()
                    if dic['topics']:
                        for each_topic in dic['topics']:
                            each_topic = each_topic.encode('utf-8').lower()
                            key = each_loc + ' : ' + each_topic
                            if key not in self.KB:
                                self.KB[key] = []
                                self.KB[key].append(dic['id'])
                            else:
                                self.KB[key].append(dic['id'])
                    else:
                        if dic['Annotation'] is not None:
                            key = each_loc + ' : '+dic['Annotation']['Type']
                            if each_loc not in self.KB:
                                self.KB[key] = []
                                self.KB[key].append(dic['id'])
                            else:
                                self.KB[key].append(dic['id'])
                        else:
                            key = each_loc + ' : '+'no topics'
                            if each_loc not in self.KB:
                                self.KB[key] = []
                                self.KB[key].append(dic['id'])
                            else:
                                self.KB[key].append(dic['id'])
            else:
                if dic['geohash'] is not None:
                    if dic['topics']:
                        for each_topic in dic['topics']:
                            each_topic = each_topic.encode('utf-8').lower()
                            key = dic['geohash']+ ' : ' + each_topic
                            if key not in self.KB:
                                self.KB[key] = []
                                self.KB[key].append(dic['id'])
                            else:
                                self.KB[key].append(dic['id'])
                    else:
                        if dic['Annotation'] is not None:
                            key = dic['geohash'] + ' : ' + dic['Annotation']['Type']
                            if key not in self.KB:
                                self.KB[key] = []
                                self.KB[key].append(dic['id'])
                            else:
                                self.KB[key].append(dic['id'])
                        else:
                            key = dic['geohash'] + ' : '+'no topics'
                            if key not in self.KB:
                                self.KB[key] = []
                                self.KB[key].append(dic['id'])
                            else:
                                self.KB[key].append(dic['id'])
        self.checkpoint += 1
        print '===check point:', self.checkpoint, '=== processing text doc:', dic['id']

    def kb_to_situation_clustering(self):
        """
        Transferring global dictionary(i.e clustering data structure) to a json-line file
        :output: .txt file
        """
        num = 1
        id_label = {}
        for k, v in self.KB.items():
            result = {}
            result['cluster' + str(num)] = v
            result['preferred_name'] = k
            self.f.write(json.dumps(result))
            self.f.write('\n')
            # print '========'+k+ '===========\n'
            for each in v:
                id_label[each] = num
                # print self.id_text[each]
            num += 1
        self.f.close()

