import argparse
from utils import load_json, load_csv, reshape_data, save_data

# MAIN EXECUTION
def main(args):
    # Load data
    data = load_json(DATA_DIR, file_name)
    dictionary = load_csv(DATA_DIR,'index_dictionary.csv')

    # Filter out non-senior dialogues
    filtered = [item for item in data if any(x in item['profile']['persona']['human'] for x in ['A03','A04'])]

    # Set instruction and source HERE
    instruction = '당신은 독거노인인 [USER]와 대화하는 [SYSTEM]입니다. 대화의 목적은 [USER]의 건강 상태와 라이프스타일을 파악하고, [USER]의 발화에 공감하는 [OUTPUT]을 생성하는 것입니다. 주어진 [INPUT]에 이어질 [OUTPUT]을 친절하고 공손한 어투로 생성하세요. [OUTPUT]을 생성할 때, [CONTEXT]에 포함된 정보를 반영하세요.'
    source = '감성대화말뭉치'

    # Reshape data
    instances = reshape_data(filtered, dictionary, instruction, source)

    # Export data
    save_data(instances, DATA_DIR, '감성대화말뭉치_reshaped.json')

if __name__ = '__main__':
    # Define arguments
    parser = argparse.ArgumentParser(description='시니어용 챗봇 학습 데이터 전처리 모듈')
    parser.add_argument('-dir','--data_directory',type=str, required=True, 
                        help='(REQUIRED) input file directory')
    parser.add_argument('-fn','--file_name',type=str, required=True, 
                        help='(REQUIRED) input file name')
    parser.add_argument('-dn','--dictionary_name',type=str, default='index_dictionary.csv', 
                        help='(OPTIONAL) index dictionary file name')
    parser.add_argument('-on','--output_name',type=str, defalut='감성대화말뭉치_reshaped.json', 
                        help='(OPTIONAL) output file name')
    args = parser.parse_args()

    main(args)