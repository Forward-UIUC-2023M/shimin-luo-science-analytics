# Science Analytics

## Overview

The codes stored in this repository is responsible for a collection of code from Shimin Luo during the time of Science Analytics group summer research. It primarily includes four main parts:

* The reproduced MVR (minimum violation rankings) algorithm [pre-task].
* Collect publication data from OpenAlex based on faculty name and institution, and integrate the data for import into the Neo4j graph database.
* Verify the data quality of OpenAlex, DBLP, and Semantic Scholar.
* Explore and utilize methods based on image and name recognition to identify the gender and ethnicity of individuals, and attempt to integrate them with Alicia's code.

## Setup

* Python 3.10.6
* pip 22.2.2
* Other dependencies are listed in `requirements.txt`, you can use the below line to install these dependencies.

```
pip install -r requirements.txt 
```

## Repo's file structure

```
shimin-luo-science-analytics/
    - .idea
    - .ipynb_checkpoints
    - pre_task/
        -- ComputerScience_edgelist.csv
        -- MVR.ipynb
    - datasets/ 
        -- faculty.json
        -- Faculty_CS_ECE-20230806.csv
    - src/
        -- data_retrival_openAlex.ipynb
        -- DBLP_test.ipynb
        -- gender_race_identification.ipynb
        -- image_based_identification.py
        -- name_based_identification.py
        -- new_data_quick_look.py
        -- semantic_test.ipynb
    - README.md
    - requirements.txt
```
## Description and Algorithmic Design 

* `pre_task/MVR.ipynb`: Replicate the MVR algorithm and validate its quality.
* `src/data_retrival_openAlex.ipynb`: Extract and cleanse data from `datasets/faculty.json`, standardize institution names, retrieve publication information through the OpenAlex API using names and institution details, and consolidate all information into three `node` data files and two `relationship` data files. Import these files into the `Neo4j` graph database.
* `src/DBLP_test.ipynb` and `src/semantic_test.ipynb`: Conducted experiments to analyze DBLP & Semantic Scholar data quality (Eg. the missing rate of affiliation)
* `src/image_based_identification.py`: Utilize the Google Search API to crawl images from faculties' websites, download image files, and employ `DeepFace` for image recognition to obtain information about the faculties' gender and ethnicity.
* `src/name_based_identification.py`: Usage of Two Methods (Ethnea, gender-guesser) for Name-based Recognition of Ethnicity and Gender.
* `gender_race_identification.ipynb`: Merging some of my code with Alicia's search process code.
* `src/new_data_quick_look.py`: Just a simple review of the data quality in the newly released dataset, `datasets/Faculty_CS_ECE-20230806.csv`: statistics on missing data in each column and the count of distinctive data in specific columns.

## Demo video



## Issues and Future Work

* While searching in OpenAlex, using the same author and institution for search might result in different records. However, these records could potentially refer to the same individual. It's important to note that in the `src/data_retrival_openAlex.ipynb` notebook, there is no entity merging operation conducted.
* The code in `src/name_based_identification.py` cannot be run directly. These three code blocks need to be integrated back into Alicia's overall code and further developed in order to run successfully.


## References 
* MVR algorithm: 
  * Aaron Clauset, Samuel Arbesman, and Daniel B. Larremore. Systematic inequality and hierarchy in faculty hiring networks. (2015)
* DeepFace: 
  * Sefik Ilkin Serengil and Alper Ozpinar. Lightface: A hybrid deep face recognition framework. (2020)
  * Sefik Ilkin Serengil and Alper Ozpinar. Hyperextended lightface: A facial attribute analysis framework. (2021)
  * Github: https://github.com/serengil/deepface
* Ethnea: 
  * Vetle Ingvald Torvik and Sneha Agarwal. Ethnea – an instance-based ethnicity classifier based on geo-coded author names in a large-scale bibliographic database. (March 2016)
  * Tool website: [Ethnea (illinois.edu)](http://abel.lis.illinois.edu/cgi-bin/ethnea/search.py)
* Google Search API:
  * Github: https://github.com/serpapi/google-search-results-python

