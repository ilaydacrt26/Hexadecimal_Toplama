def uzunlukEsitle(say1,say2): # büyük değer, küçük değer
    while len(say1) != len(say2):
        say2 = "0" + say2
    return say2
        
def topla(sayi1,sayi2):
    degerler = {'0':'0','1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9','A':'10','B':'11','C':'12','D':'13','E':'14','F':'15'}
    sonuclar = {'0':'0','1':'1','2':'2','3':'3','4':'4','5':'5','6':'6','7':'7','8':'8','9':'9','10':'A','11':'B','12':'C','13':'D','14':'E','15':'F'}

    elde = 0
    sonuc = 0
    ek = 0
    
    j = max(len(sayi1),len(sayi2))-1
    
    for i in range(max(len(sayi1),len(sayi2))):
        
        toplam = int(degerler[sayi1[j]]) + int(degerler[sayi2[j]])
        
        if toplam%16 + elde == 16:
            ek = 1
            eklenecek = 0
        else:
            eklenecek = (sonuclar[str(toplam%16 + elde + ek)])
            ek = 0
               
        if i==0:
            sonuc = eklenecek
        else:
            sonuc = str(eklenecek) + str(sonuc)
                        
        elde = 0
        elde = int(toplam/16)
                        
        if i==len(sayi1)-1 and elde != 0 :
            sonuc = str(elde) + str(sonuc)
               
        j-=1
        
    return sonuc

sayi1 = input("Birinci degeri girin : ")
sayi2 = input("İkinci değeri girin : ")
        
if len(sayi1) > len(sayi2):
    sayi2 = uzunlukEsitle(sayi1,sayi2)
    sonuc = topla(sayi1,sayi2)
else:
    sayi1 = uzunlukEsitle(sayi2,sayi1)
    sonuc = topla(sayi1,sayi2)
        
print("sonuc : " + sonuc)