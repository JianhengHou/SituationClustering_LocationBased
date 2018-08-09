# Introduction
This is a basic demo of situation clustering model on streaming data on tweets. 
# Guide
The model takes .txt file, in which all data represents like json lines in time sequence, as the input. Meanwhile, one should specify the output file as one run the model. There is another optional parameter, -stop_point, which is used to specify that how many tweets would be processed in the model. All tweets would be processed by default, if one do not want to set stop point.

One input file and two output files are in the repository as samples for users. One of output file is one , the other is one with setting stop_point parameter.

# Example

If all tweets need to be processed, commend should be like this:

	python SituationClustering.py -input input_sample.txt -output result.txt
	
If one wants to set stop point to run the code, commend should be like this:

	python SituationClustering.py -input input_sample.txt -output result.txt -stop_point 500
