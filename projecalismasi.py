class library:
   result = open("books.txt", "a+")
   print(result)
   file= open("books.txt", "a+", encoding='utf-8')
   file.close()
listBooks=[]
booknameList=[]
writerList=[]
pagesList=[]

def listBooks():
   print("Tüm Kitapların Listesi")
   print(f"{'Kitap Adı'} {'Yazar Adı'} {'Sayfa Sayısı'}")

   for sn in range(len(listBooks)):
    print(f"{booknameList[sn]} {writerList[sn]} {pagesList[sn]}")
   
def addBooks():
   bookname= input("Kitap Adını Girin:")
   writer= input("Kitap Yazarını Girin:")
   pages= int(input("Kitabın Sayfa Sayısını Girin:"))
   booknameList.append(bookname)
   writerList.append(writer)
   pagesList.append(pages)
   print("Kitap Ekleme Başarılı")
def removeBooks():
   print("Kitap Silme İşlemi")
   bookname= input(" Silinecek Kitap Adını Girin:")
   if bookname in booknameList:
      silinecekSn= booknameList.index(bookname)
      booknameList.pop(silinecekSn)
      writerList.pop(silinecekSn)
      pagesList.pop(silinecekSn)
      print("Silme İşlemi Başarıyla Gerçekleşti")
   else:
      print("Silmek İstediğiniz Kitap Listede Kayıtlı Değil")

def menu():
 fonksiyonListesi=[listBooks, addBooks, removeBooks]
 while True:
   print(" 1- Kitapları Listele")
   print(" 2- Kitap Ekle")
   print("3- Kitap Sil")
   print("0- Programdan Çık")
   seciminiz= int (input("Lütfen Yapmak İstediğiniz İşlemi Seçiniz (0-3):" ))
   print("\n"*40)
   if seciminiz <= 3 and seciminiz >=1:
      fonksiyonListesi[seciminiz-1]()
     
   elif seciminiz==0:
      print("Çıkış Yapılacak")
      break 
   else:
      print("Lütfen Seçim İçin 0 ile 3 arası bir rakam giriniz!")
menu()



