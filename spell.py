from contextlib import suppress
from flask import *
from spellchecker import *
from tabledef import *
import easygui

def spellCheck():
    if "OpenFile" in request.form:
        try:
            fileType = ".txt"
            fileEnd = "*"+fileType
            spellChecker = SpellChecker()
            misspelledStr = ""
            
            filePathList = easygui.fileopenbox("Select the "+fileType+" file you would like to spellcheck.",fileEnd,fileEnd,"False")
            
            with suppress(TypeError):
                filePathStr = ''.join(filePathList)
                
            if (filePathList == None):
                return("No file was selected to spellcheck")
                
            else:
                file = open(filePathStr,"r")
                fileContentList = file.read().split(' ')
                file.close()
                
                misspelled = spellChecker.unknown(fileContentList)
                wordTotal = len(fileContentList)
                wordTypo  = len(misspelled)
                percTypo  = "{:.1%}".format(wordTypo/wordTotal)
                for word in misspelled:
                    misspelledStr = '\n\n'+misspelledStr +''+word+' -->'+spellChecker.correction(word)+'   '
                return render_template('spellcheck.html', contentList=fileContentList, typoList=misspelledStr, totalCount=wordTotal, typoCount=wordTypo, typoPercent=percTypo)
        except:
            raise
            
    else: 
        pass
    return
