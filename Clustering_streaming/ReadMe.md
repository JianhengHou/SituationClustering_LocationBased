{\rtf1\ansi\ansicpg936\cocoartf1504\cocoasubrtf830
{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 This is a basic demo of streaming version code of situation clustering.  It takes a JSON-line file as an input, but can be seen like a simulation of streaming through processing algorithm line by line so to form the basic framework of codes in practice.\
\
\
1. Initialize the algorithm and assign input file (JSON line)and output file (situation clustering result)\
\
SC = SituationCluserting(input_path, output_path)\
\
2. Run the situation clustering algorithm (GPE based)\
\
SC.run()\
\
3. If necessary, one can check the clustering report after running the algorithm via:\
\
SC.analysis_result()}