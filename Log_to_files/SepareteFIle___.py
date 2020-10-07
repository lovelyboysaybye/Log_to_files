import re
import time
import os
import wave
import struct
import threading

import json

from pprint import pprint
count_value = 0
folder = None
check = None

class Zapys:
    def __init__(self, element, timee):
        self.timee = str(timee)
        elements = element.split(" ")
        self.number = elements[1]
        self.type_of = elements[0]
        self.word = elements[2]
        self.frame_num = elements[3]
        self.frame_size = elements[4]
        if (element[-1] == " "):
            self.data = elements[5:-1]
        else:
            self.data = elements[5:]
        self.data = [int(item) for item in self.data]

    def make(self):
        self.result = []
        i = 0
        if self.type_of == 'S':
            while i < (len(self.data)):
                if self.data[i] != 0 :
                    self.result.append(self.data[i])
                else:
                    zeros = [0 for j in range(self.data[i + 1])]
                    self.result.extend(zeros)
                    i += 1
                i += 1
        elif self.type_of == 'W':
            self.result = self.data

        print("ok4")
        dict = {"label": self.word, "values": self.result}
        if self.type_of == 'W':
            filename = self.number + self.type_of + self.word + str(int(self.frame_num) * int(self.frame_size))
            sub_fold = 'Waves'

        elif self.type_of == 'S':
            filename = self.number + self.type_of + self.word + str(int(self.frame_num) * int(self.frame_size) + 2)
            dict.update({"frame_num": self.frame_num, "frame_size": self.frame_size})
            sub_fold = "Spect"
    
        num = self.timee
        print("ok5")
        os.makedirs(name=folder + "/" + num + "/" + sub_fold)


        with open(folder + "/" + num + "/" + sub_fold + "/" + filename + ".json", 'w+') as fp:
            json.dump(dict, fp)


def SplitFiles(path,str, timee):
    global count_value
    global folder
    global check

    try:
        with open(path, 'r') as file:
            text = file.read()
        text = text.split("\n")

        if (text[-1] == ""):
            text = text[:-1]
        print("ok1")
        tti = str(timee)
        print(tti)
        folder = "results"
        print("ok2")

        if (os.path.exists(fodler) == False):
            os.makedirs(name=folder)
            os.makedirs(name=folder + "/" + tti)


        print("ok3")
        couples = len(text)
        index = 0


        print(len(text))
        for element in text:
            zapys = Zapys(element, tti)
            zapys.make()
            count_value = (index) / (couples - 1 ) * 100
            index += 1
        check = None
        count_value = -1
    except:
        print("errorrrrrr hereeeee")
        check = False


  
def clear_count():
    global count_value
    count_value = 0

def get_check():
    global check
    return check

def get_folder():
    global folder
    return folder

def set_check_True():
    global check
    check = True

def set_check_None():
    global check
    check = None

