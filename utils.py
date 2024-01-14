import os
import csv
import json
from tqdm import tqdm
import time

def load_json(DATA_DIR, file_name):
    with open(os.path.join(DATA_DIR, file_name)) as f:
        data = json.load(f)
    f.close

    return data

def load_csv(DATA_DIR, file_name):
    with open(os.path.join(DATA_DIR, file_name), encoding='utf-8') as f:
        reader = csv.reader(f)
        data = list(reader)
        data = {item[1]: item[0] for item in data[1:]}
    f.close()

    data['D01'] == '만성질환 있음'
    data['D02'] == '만성질환 없음'

    return data

def reshape_data(DATA, DICTIONARY, instruction, source):
    start = time.time()

    data = []
    for item in tqdm(DATA):
        # Parse out context information
        situation = DICTIONARY[item['profile']['emotion']['situation'][0]]
        emotion = DICTIONARY[item['profile']['emotion']['type']]
        disease = DICTIONARY[item['profile']['emotion']['situation'][1]]

        CONTEXT = [situation, emotion, disease]

        # Reshape conversations
        dialogues = []
        for user, system in zip(['HS01','HS02','HS03'],['SS01','SS02','SS03']):
            user_utterance = item['talk']['content'][user]
            system_response = item['talk']['content'][system]

            dialogue = [f"[USER] {user_utterance}", f"[SYSTEM] {system_response}"]
            dialogues.extend(dialogue)

            INPUT = ' '.join(map(str, dialogues[:-1]))
            OUTPUT = dialogues[-1].replace('[SYSTEM] ','')

            # Put together to generate a conversation instance
            instance = {}
            instance['source'] = source
            instance['instruction'] = instruction
            instance['input'] = INPUT
            instance['output'] = OUTPUT
            instance['context'] = CONTEXT

            data.append(instance)
    
    print("총 실행시간 : {:.4f} sec".format(time.time()-start))

    return data

def save_data(data, DATA_DIR, file_name):
    with open(os.path.join(DATA_DIR,file_name),'w') as f:
        json.dump(data, f)
    f.close()