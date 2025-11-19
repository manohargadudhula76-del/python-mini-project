import qrcode
data=input("enter the text or url to generate the qr code ")
qr=qrcode.make(data)
qr.save("my_qr_code.png")
qr
