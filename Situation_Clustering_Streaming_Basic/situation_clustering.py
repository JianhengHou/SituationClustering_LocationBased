# coding: utf-8

'''

Codes between the '*' are data structures which are used for getting the precision recall and f score

'''

# from GPE import *
# from GPE_topics1 import *
from GPE_topics2 import *


class SituationClustering():
    def __init__(self, input_path, output_path, input_size=0, model_name=None):
        self.output_path = output_path
        self.input_size = input_size
        try:
            self.input_file = open(input_path, 'r')
        except IOError:
            print "Error: Cannot find the input file or the input file is not readable."

        try:
            if model_name == 'GPE':
                self. model = GPE(self.output_path)
            elif model_name == 'GPE_topics1':
                self.model = GPE_topics1(self.output_path)
            elif model_name == 'location+topics':
                self.model = GPE_topics2(self.output_path)
        except IOError:
            print "Error: Please select a situation clustering model."

    def run(self):
        """
        The main function, including three frames: read_json, update_kb, kb_to_situation_clustering
        """
        count = 0
        while True:
            line = self.input_file.readline()
            count += 1
            if line:
                dic = json.loads(line)
                self.model.update_kb(dic)
            else:
                break
            if count == self.input_size:
                break
        self.input_file.close()
        self.model.kb_to_situation_clustering()
        # self.model.result_plot()


SC = SituationClustering(input_path='test_streaming_all.txt',
                         output_path='clustering_result_streaming_basic(gpe_geo_topics_type).txt', input_size=10000,
                         model_name='location+topics')
SC.run()