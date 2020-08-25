from __future__ import unicode_literals
import speech_recognition as sr
# from pydub import AudioSegment
import array
import csv
import os
import numpy as np
from django.shortcuts import redirect, render, HttpResponse
from fuzzywuzzy import fuzz
from gtts import gTTS
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt


#Global Variable
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UPLOAD_DIR = os.path.abspath(os.path.join(BASE_DIR, '../../easeassist/uploads'))
defult_file_path = os.path.abspath(os.path.join(BASE_DIR, '../../easeassist/files'))

def callS2T(request):
   a = s2t(UPLOAD_DIR+'/test.wav')
   print(a)
   return HttpResponse(a)

#For getting value form php->py via Django
@csrf_exempt
def message_from_php(request):
   if(request.method == "POST"):
      if(request.POST.get('type')=="voice"):
         print(UPLOAD_DIR+'/test.wav')
         answer= s2t(UPLOAD_DIR+'/test.wav') #s2t(request.POST.get('voice_file'))
         # if request.POST.get('qacsv') == 0:
         #    print("CSV is not available")
         # else:
         #    file_path=request.POST.get('qacsv')
         #    output = []
         #    output = string_check(answer,file_path)
         #    for val in output.items():
         #       print(val)
         #    output = output.update({2:answer})
         #    print (output)
         # return JsonResponse(output)
         return HttpResponse(answer)
      elif(request.POST.get('type')=="text"):
         if request.POST.get('qacsv') == 0:
               print ("data is not available")
         else:
            file_path=request.POST.get('qacsv')
            output = []
            output = string_check(request.POST.get('message'),file_path)
            # return HttpResponse(json.dumps(output))
            print("output ",json.dumps(output))
            return JsonResponse(output)
            # return json.dumps(output)

##################################################
# PYTHON CODE FOR DATA MANULAPTION#
#php_csv->py_2darray
def csv_py(file_path):
   datafile = open(file_path, 'r')
   datareader = csv.reader(datafile, delimiter=str(u','))
   qacsv = []
   for row in datareader:
      qacsv.append(row)       
   #CSV->Python Array
   i=0
   for q,w,e in qacsv:
      qacsv[i][0]= int(q)
      i=i+1
   # print ( "Type cast array" , qacsv)
   return qacsv

#NLP via fuzz
def string_check(user_input,file_path):
   Similar_found = False
   threshold_value = 40
   final_output = []
   #funcation for CSV->py
   file_path=defult_file_path+'/'+file_path
   qacsv=csv_py(file_path)
   percsv= np.zeros((len(qacsv), 2))
   # print (percsv)
   #finding the similarity % 
   f=g=0
   for i,j,q in qacsv:
      percsv[f][0]=qacsv[f][0]
      percsv[f][1]=fuzz.ratio(qacsv[f][1],user_input)
      f=f+1
   #Finding Biggest val
   maxincols=np.amax(percsv, axis=0)
   if(threshold_value>=maxincols[1]):
      return "Not found"
   else:
      for i,j in percsv:
         if(maxincols[1]==j):
            for q,w,e in qacsv:
               if(i==q):
                  final_output.append(q)
                  final_output.append(w)
                  final_output.append(e)
      jsdata = {"results": final_output}
   return jsdata

#voice->text
def s2t(voice):
   print("voice = "+voice)
   r = sr.Recognizer()
   with sr.AudioFile(voice) as source:
      audio = r.record(source)    
   try:
      texxt = r.recognize_google(audio)
      print("text = "+texxt)
      return texxt
   except sr.UnknownValueError:
      return "Speech Recognition could not understand audio"
   except sr.RequestError as e:
      return "Could not request results from Speech Recognition service; {0}".format(e)

#Text->voice
def T2S(text_message,file_name):
    language = 'en'
    output = gTTS(text=str(text_message), lang=language)
    output.save(file_name+".mp3")
   # r = sr.Recognizer()

   # file_audio = sr.AudioFile(file_name+".wav")
   # with file_audio as source:
   #    audio_text = r.record(source)
   # print(type(audio_text))
   # print(r.recognize_google(audio_text))

# T2S("hello moto","test")
# print (a)





