# 감성대화 말뭉치 전처리

- preprocessing.py file preprocesses and reshaped 감성대화 말뭉치 to be used to train chatbots.

---

## ARGS (all fields are optional)
- `--data_directory`, `-dir` corresponds to the input file directory (STR, required)
- `--file_name`, `-fn` corresponds to the input file name (STR, required)
- `--dictionary_name`, `-dn` corresponds to the index dictionary file name (STR)
    - if not specified, then set to **index_dictionary.csv**
- `--output_name`, `-on` corresponds to the output file name (STR)
    - if not specified, then set to **index_dictionary.csv**

---

## EXECUTION
- On terminal, run the following (add arguments as desired)
 ```python
 python main.py -dir "data directory" -fn "input file name" [-dn "dictionary file name" -on "output file name"]
 ```

 - DEPENDENCY CHECK: runs on python 3.11.7
 
