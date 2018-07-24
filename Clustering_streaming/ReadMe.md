This is a basic demo of streaming version code of situation clustering.  It takes a JSON-line file as an input, but can be seen like a simulation of streaming through processing algorithm line by line so to form the basic framework of codes in practice.


1. Initialize the algorithm and assign input file (JSON line)and output file (situation clustering result)\

SC = SituationCluserting(input_path, output_path)

2. Run the situation clustering algorithm (GPE based)

SC.run()

3. If necessary, one can check the clustering report after running the algorithm via:\

SC.analysis_result()}