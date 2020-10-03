#! / usr / bin / env python3
# - * - kodlama: utf-8 - * -

ithalat  istekleri
dan  os  ithalat  sisteminden  olarak  s



banner  =  "" "
| Hergun'a göre İstediginiz telefon 1 defa mesaj atma hakkınız vardır
| Mesajınız karakter sayısı sınırlı bunu mesajınızı yazdıktan sonra görüceksiniz.
| Tel adresinizi Doğru girmezseniz hata alabilrsiniz.
"" "

baskı ( afiş )

sor  =  input ( "Tel adresi Örn: +905555555555 >>>" )

mesaj  =  input ( "Mesajınız >>>" )

arlk  =  mesaj [ 0 : 70 ]

print ( " \ n | Mesajınızın Gönderilebilecek kısmı aşagıdaki gibidir. \ n " + arlk )

drlm  =  input ( " \ n | Mesajınız Gönderilsinmi? [y / n] >>>" )

Eğer  drlm  ==  "y"  veya  drlm  ==  "Y" :
    baskı ( " \ n " + sor + " \ n " + arlk + " \ n " )
    resp  =  istekler . gönderi ( 'https://textbelt.com/text' , {
  'telefon' : sor ,
  'mesaj' : arlk ,
  'key' : 'textbelt' ,
    })
    baskı ( solunum . json ())

elif  drlm  ==  "n"  veya  drlm  ==  "N" :
    çık ()
başka :
    print ( " \ n | Hata yaptınız." )
