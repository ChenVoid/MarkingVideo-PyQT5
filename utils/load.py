import csv
import os

from config import usrConfig


def load_que(video_name):
    videoList = os.listdir(usrConfig.QuestionsPath)
    ansList = []
    if video_name + '.csv' in videoList:
        with open('./csv/questions/' + video_name + '.csv', mode='r', encoding='gb2312', newline='') as report:
            reader = csv.reader(report)
            for raw in reader:
                ansList.append(raw)
        return True, ansList
    else:
        return False, ansList


'''
    try:
        with open('./csv/questions/' + video_name + '.csv', mode='r', encoding='gb2312', newline='') as report:
            reader = csv.reader(report)
            ansList = []
            for raw in reader:
                ansList.append(raw)
        return ansList
        # return True, None
    except Exception:
        import traceback
        return False, traceback.print_exc()
'''
