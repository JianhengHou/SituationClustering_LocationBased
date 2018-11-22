# coding: utf-8

'''

Codes between the '*' are data structures which are used for getting the precision recall and f score

'''

import sys
from LocationTopics import *


class SituationClustering():
    def __init__(self, input_path, output_path, stop_point=0):
        self.output_path = output_path
        self.stop_point = stop_point
        self.model = LocationTopics(self.output_path)
        try:
            self.input_file = open(input_path, 'r')
        except IOError:
            print "Error: Cannot find the input file or the input file is not readable."

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
            if count == self.stop_point:
                break
        self.input_file.close()
        self.model.kb_to_situation_clustering()


input_value = ''
output_value = ''
stopPoint = 0
if len(sys.argv) >= 3:
    if sys.argv[1] == '-input' and sys.argv[2]:
        input_value = sys.argv[2]
    if len(sys.argv) >= 5:
        if sys.argv[3] == '-output' and sys.argv[4]:
            output_value = sys.argv[4]
        if len(sys.argv) == 7:
            if sys.argv[5] == '-stop_point' and sys.argv[6]:
                stop_point = sys.argv[6]

SC = SituationClustering(input_path=input_value, output_path=output_value, stop_point=stopPoint)
SC.run()