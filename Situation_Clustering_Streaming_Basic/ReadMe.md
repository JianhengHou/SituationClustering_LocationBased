{\rtf1\ansi\ansicpg936\cocoartf1504\cocoasubrtf830
{\fonttbl\f0\fnil\fcharset0 HelveticaNeue;\f1\fnil\fcharset134 .PingFangSC-Regular;\f2\fswiss\fcharset0 Helvetica;
}
{\colortbl;\red255\green255\blue255;\red27\green31\blue34;\red255\green255\blue255;}
{\*\expandedcolortbl;;\cssrgb\c14118\c16078\c18039;\cssrgb\c100000\c100000\c100000;}
{\*\listtable{\list\listtemplateid1\listhybrid{\listlevel\levelnfc0\levelnfcn0\leveljc0\leveljcn0\levelfollow0\levelstartat1\levelspace360\levelindent0{\*\levelmarker \{decimal\}.}{\leveltext\leveltemplateid1\'02\'00.;}{\levelnumbers\'01;}\fi-360\li720\lin720 }{\listname ;}\listid1}
{\list\listtemplateid2\listhybrid{\listlevel\levelnfc0\levelnfcn0\leveljc0\leveljcn0\levelfollow0\levelstartat2\levelspace360\levelindent0{\*\levelmarker \{decimal\}.}{\leveltext\leveltemplateid101\'02\'00.;}{\levelnumbers\'01;}\fi-360\li720\lin720 }{\listname ;}\listid2}
{\list\listtemplateid3\listhybrid{\listlevel\levelnfc0\levelnfcn0\leveljc0\leveljcn0\levelfollow0\levelstartat3\levelspace360\levelindent0{\*\levelmarker \{decimal\}.}{\leveltext\leveltemplateid201\'02\'00.;}{\levelnumbers\'01;}\fi-360\li720\lin720 }{\listname ;}\listid3}}
{\*\listoverridetable{\listoverride\listid1\listoverridecount0\ls1}{\listoverride\listid2\listoverridecount0\ls2}{\listoverride\listid3\listoverridecount0\ls3}}
\margl1440\margr1440\vieww21000\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\sl360\sa320\partightenfactor0

\f0\fs32 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 This is a basic demo of streaming version code of situation clustering based on location + topics. It takes a JSON-line file as an input file
\f1 ,
\f0  but can be seen like a simulation of streaming situation clustering through running algorithms on text docs line by line so to form the basic framework of codes in practice.\
\pard\tx220\tx720\pardeftab720\li720\fi-720\sl360\partightenfactor0
\ls1\ilvl0\cf2 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	1.	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Initialize the model and assign input file 
\f1 (
\f0 JSON line
\f1 ),
\f0  output file 
\f1 (
\f0 situation clustering result
\f1 ), the model to use, and maybe indicate the number of json lines to read (this is optional) :
\f0 \cb1 \
\pard\pardeftab720\sl360\sa320\partightenfactor0
\cf2 \cb3 	\
	SC = SituationCluserting
\f1 (
\f0 input_path
\f1 ,
\f0  output_path
\f1 ,
\f0  
\f2 \cf0 \cb1 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 model_name, 
\f1 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 [
\f0 input_size
\f1 ])\

\f0 e.g. 
\f2 \cf0 \cb1 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 SC = SituationClustering(	 input_path='test_streaming_all.txt', \
						 output_path='clustering_result_streaming_basic(gpe_geo_topics_type).txt', \
						 input_size=10000,\
						 model_name='location+topics')\

\f0 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 \
\pard\tx220\tx720\pardeftab720\li720\fi-720\sl360\partightenfactor0
\ls2\ilvl0\cf2 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	2.	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 Run the situation clustering algorithm 
\f1 (
\f0 location + topics
\f1 )
\f0 \cb1 \
\pard\pardeftab720\sl360\sa320\partightenfactor0
\cf2 \cb3 	\
	SC.run
\f1 ()\

\f0 \
\pard\tx220\tx720\pardeftab720\li720\fi-720\sl360\partightenfactor0
\ls3\ilvl0\cf2 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	3.	}\expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 If necessary
\f1 ,
\f0  one can check the clustering result by uncommenting the codes in the function: LocationTopics.kb_to_situation_cluserting\
}