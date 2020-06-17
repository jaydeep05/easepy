<<<<<<< HEAD
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

defult_file_path = "/Applications/XAMPP/htdocs/php/easeassist/files/";
# php_server_ip = "http://localhost/php/SGH000699/Hackathon_php/ease/";
###################################
#For Sending the Value to py->php via Django
@csrf_exempt
def message_from_dj(request,message):
   #sample_test
   # data_py = str(csv_py("/mnt/d/Projects/python lib/persons.csv"))
   # final_respose = "http://hackthon_php/test_UserInput.php?message="+data_py
   #end_sameple
   i=1
   for arg in message: 
      if i==1:
         final_message = "val"+str(i)+"="+str(arg) 
      else:
         final_message = final_message+"&val"+str(i)+"="+str(arg)
      i=i+1
   final_respose = php_server_ip+"last_page.php?"+final_message
   print (final_respose)
   response = redirect(final_respose)
   return response
   # return render(request,'http://192.168.43.99/test.php?message="test from dj->ph"') 

def callS2T(request):
   a= s2t("/Applications/XAMPP/htdocs/php/SGH000699/Hackathon_php/ease/uploads/test.wav")
   # print(a)
   return HttpResponse("<h1>MyClub Event Calendar</h1>")

#For getting value form php->py via Django
@csrf_exempt
def message_from_php(request):
   #Smaple_Message_from_php
   # raw_message_php = request.POST.get['message']
   # print raw_message_php
   #End_smaple
   print(request.POST.get('type'))
   print(request.POST.get('message'))
   print(request.POST.get('qacsv'))
   if(request.method == "POST"):
      if(request.POST.get('type')=="voice"):
         answer=s2t(request.POST.get('voice_file'))
         if "#error#" in answer:
            message_from_dj(request,answer)
         else:
            if request.POST.get('qacsv') is 0:
               print("CSV is not available")
            else:
               file_path=request.POST.get('qacsv')
               output = []
               output = string_check(answer,file_path)
               # return message_from_dj(request,output)
               print (JsonResponse(output))
            return JsonResponse(output)
      elif(request.POST.get('type')=="text"):
         if request.POST.get('qacsv') is 0:
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





=======
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
#JD
# defult_file_path = "/Applications/XAMPP/htdocs/php/easeassist/files/";
#Vraj
defult_file_path = "/mnt/d/Projects/XAMPP/htdocs/php/easeassist/files/";
# php_server_ip = "http://localhost/php/SGH000699/Hackathon_php/ease/";
###################################
#For Sending the Value to py->php via Django
@csrf_exempt
def message_from_dj(request,message):
   #sample_test
   # data_py = str(csv_py("/mnt/d/Projects/python lib/persons.csv"))
   # final_respose = "http://hackthon_php/test_UserInput.php?message="+data_py
   #end_sameple
   i=1
   for arg in message: 
      if i==1:
         final_message = "val"+str(i)+"="+str(arg) 
      else:
         final_message = final_message+"&val"+str(i)+"="+str(arg)
      i=i+1
   final_respose = php_server_ip+"last_page.php?"+final_message
   print (final_respose)
   response = redirect(final_respose)
   return response
   # return render(request,'http://192.168.43.99/test.php?message="test from dj->ph"') 

def callS2T(request):
   a= s2t("/Applications/XAMPP/htdocs/php/SGH000699/Hackathon_php/ease/uploads/test.wav")
   # print(a)
   return HttpResponse("<h1>MyClub Event Calendar</h1>")

#For getting value form php->py via Django
@csrf_exempt
def message_from_php(request):
   #Smaple_Message_from_php
   # raw_message_php = request.POST.get['message']
   # print raw_message_php
   #End_smaple
   print(request.POST.get('type'))
   print(request.POST.get('message'))
   print(request.POST.get('qacsv'))
   if(request.method == "POST"):
      if(request.POST.get('type')=="voice"):
         answer=s2t(request.POST.get('voice_file'))
         if "#error#" in answer:
            message_from_dj(request,answer)
         else:
            if request.POST.get('qacsv') is 0:
               print("CSV is not available")
            else:
               file_path=request.POST.get('qacsv')
               output = []
               output = string_check(answer,file_path)
               # return message_from_dj(request,output)
               print (JsonResponse(output))
            return JsonResponse(output)
      elif(request.POST.get('type')=="text"):
         if request.POST.get('qacsv') is 0:
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
   file_path=defult_file_path+file_path
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
   r = sr.Recognizer()
   with sr.AudioFile(voice) as source:
       audio = r.record(source)   
     
   try: 
       print(r.recognize_google(audio)) 
     
   except sr.UnknownValueError: 
       print("Google Speech Recognition could not understand audio") 
     
   except sr.RequestError as e: 
       print("Could not request results from Google Speech Recognition service; {0}".format(e))   

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





>>>>>>> 97f25a8b60985e7c31992a520d61cd3b87f25943
