# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 15:08:11 2023

@author: s20553
"""

from nltk import ngrams
import string
import re
import unicodedata
liste = [
'BAŞVURU'
,'TESCİL'
,'2. YIL SİCİL KAYIT'
,'3. YIL SİCİL KAYIT'
,'4. YIL SİCİL KAYIT'
,'5. YIL SİCİL KAYIT'
,'6. YIL SİCİL KAYIT '
,'7. YIL SİCİL KAYIT'
,'8. YIL SİCİL KAYIT'
,'9. YIL SİCİL KAYIT'
,'10. YIL SİCİL KAYIT'
,'11. YIL SİCİL KAYIT'
,'12. YIL SİCİL KAYIT'
,'13. YIL SİCİL KAYIT'
,'15. YIL SİCİL KAYIT'
,'16. YIL SİCİL KAYIT'
,'17. YIL SİCİL KAYIT'
,'18. YIL SİCİL KAYIT'
,'19. YIL SİCİL KAYIT'
,'20. YIL SİCİL KAYIT'
,'ARAŞTIRMA TALEBİ'
,'1. İNCELEME TALEBİ'
,'2. İNCELEME TALEBİ'
,'3. İNCELEME TALEBİ'
,'ŞEKLİ İNCELEME'
,'ÖN İNCELEME TALEBİ'
,'YANIT HAZIRLAMA'
,'marka tescil belgesi'
,'ULUSAL AŞAMAYA GEÇİŞ'
,'Marka başvuru'
,'PATENT BELGESİ DÜZENLENMESİ'
,'ÖN İNCELEME ONAY RAPORU BİLDİRİMİ'
,'VEKİL DEĞİŞİKLİK TALEBİ'
,'BAŞVURU+ARAŞTIRMA+İNCELEME'
,'ARAPÇA TERCÜME'
,'DANIŞMAN FİRMA KOMİSYON BEDELİ'
,'İTİRAZ'#ben değiştirdim
,'ingilizce tercüme'
,'DİĞER ÖDEMELER'
,'İNCELEME TALEBİ'
,'DAMGA VERGİSİ BEDELİ'
,'VEKİLLİK ÜCRETİ'
,'KONSOLOSLUK VE DANIŞMANLIK ÜCRETİ'
,'EKSİK KALAN TEŞVİK ÖDEMESİ'
,'MARKA TESCİL YENİLEME'
,'PATENT BELGESİ DÜZENLENMESİ'
,'ALMANCA TERCÜME'
,'FRANSIZCA TERCÜME'
]
liste_2=[]
for text in liste:
    text = text.translate(str.maketrans('', '', string.punctuation))
    words_list=[]
    words_list = text.split()
    for index in range(len(words_list)):
        words_list[index]=words_list[index].lower()
        result = ""
        for char in words_list[index]:
            if unicodedata.combining(char):
                continue
            result += char
        if result!="":
            words_list[index]=result
        words_list[index]=words_list[index].replace('ı','i')
    with open("stop_words.txt", "r") as t:
        stop_words = t.read().splitlines()
        words_list = [w for w in words_list if not w in stop_words]
    liste_2.append(words_list)
#[print(c) for c in liste_2]

classes=list([] for i in range(max([len(a.split()) for a in liste])))

for text in liste:
    text = text.translate(str.maketrans('', '', string.punctuation))
    words_list=[]
    words_list = text.split()
    for index in range(len(words_list)):
        words_list[index]=words_list[index].lower()
        result = ""
        for char in words_list[index]:
            if unicodedata.combining(char):
                continue
            result += char
        if result!="":
            words_list[index]=result
        words_list[index]=words_list[index].replace('ı','i')
    with open("stop_words.txt", "r") as t:
        stop_words = t.read().splitlines()
        words_list = [w for w in words_list if not w in stop_words]
        
    classes[len(words_list)-1].append(words_list)
    
#[print(c) for c in classes]


def func(ngrams,number):
    global answer
    for ngram in ngrams:
        for one_class in classes[number-1]:
            if number!=1:
                if ngram[0]==one_class[0]:
                    for i in range(1,number):
                        if ngram[i]==one_class[i]:
                            if i == number-1:
                                add=" ".join(one_class)
                                writelist.append(add)
                                
                                answer=one_class
                                #print(*[i for i in one_class])
                                return 
                            continue
                        else:
                            break
            else:
                if one_class[0]==ngram:
                    writelist.append(ngram)
                    #print(ngram)
                   
                    answer=one_class
                    return 
    if number<2:
        return
    func(ngram_list[number-2],number-1)
                
pattern = r"\b\d{1,2}\w+"
writelist=[]
basvuru1='başvurusu'
basvuru2='başvurusunun'
talebi1='talebinin'
tercume1='tercümesinin'
belgesi1='belgesinin'
with open("data.txt", "r",encoding="utf-8") as file:
    for sentence in file:
        done=0
        #noktalama
        sentence = sentence.translate(str.maketrans('', '', string.punctuation))
        global_words=[]
        #kelimelere ayır
        global_words = sentence.split()
        #küçük harf yap
        for index in range(len(global_words)):
            global_words[index]=global_words[index].lower()
            result = ""
            for char in global_words[index]:
                if unicodedata.combining(char):
                    continue
                result += char
            if result!="":
                global_words[index]=result
            global_words[index]=global_words[index].replace('ı','i')
        
        #stop wordleri çıkar
        #print(global_words)
        with open("stop_words.txt", "r") as t:
            stop_words = t.read().splitlines()
            
        global_words = [w for w in global_words if not w in stop_words]
        
        for i in range(len(global_words)):
            if global_words[i] == basvuru1 or global_words[i] == basvuru2:
                global_words[i]='başvuru'
            if global_words[i] == talebi1 :
                global_words[i]='talebi'
            if global_words[i] == tercume1 :
                global_words[i]='tercüme'
            if global_words[i] == belgesi1 :
                global_words[i]='belgesi'
                
        for i in range(len(global_words)):
            result = re.findall(pattern, global_words[i])
            if result !=[]:
                new=[]
                for a in range(i):
                    new.append(global_words[a])
                for match in result:
                    count=0
                    for index in range(len(match)):
                        try:
                            a=int(match[index])
                            count+=1
                        except:
                            break
                    new.append(match[0:count])
                    if len(match[count:])!=0:
                        new.append(match[count:])
                    
                for a in range(i+1,len(global_words)):
                    new.append(global_words[a])
                global_words=new
            
        ngram_list=[]
        ngram_list.append(global_words)
        for i in range(2, len(classes)+1):
            ngram = []
            for a in list(ngrams(global_words, i)):
                ngram.append(a)    
            ngram_list.append(ngram)
            
        #print("----------",global_words)
        add = " ".join(global_words)
        writelist.append(add)
        lenght=len(classes)
        #[print(c) for c in ngram_list]
        func(ngram_list[lenght-1],lenght)     
        for i in range(len(liste_2)):
            if liste_2[i]==answer:
                index=i
                
        
        
        
#with open("output.txt", "w",encoding="utf-8") as file:
    #file.writelines(line + "\n" for line in writelist) 
        



    
