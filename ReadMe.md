This is a basic demo of streaming version code of situation clustering based on location + topics. It takes a JSON-line file as an input file, but can be seen like a simulation of streaming situation clustering through running algorithms on text docs line by line so to form the basic framework of codes in practice.

1. Initialize the model and assign input file (JSON line), output file (situation clustering result), the model to use, and maybe indicate the number of json lines to read (this is optional) :
	SC = SituationCluserting(input_path, output_path, model_name, [input_size])
	
	e.g. SC = SituationClustering(	 input_path='test_streaming_all.txt', 
						 output_path='clustering_result_streaming_basic(gpe_geo_topics_type).txt', 
						 input_size=10000,
						 model_name='location+topics')

2.	Run the situation clustering algorithm (location + topics)
	
	SC.run()

3.	If necessary, one can check the clustering result by uncommenting the codes in the function: LocationTopics.kb_to_situation_cluserting
