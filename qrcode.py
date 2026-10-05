import qrcode
import random

#please all students are requested to type their name in the list
members=['Aman','Aanchal','Anisha','Avneesh','arshi']
winner=random.choice(members)
print(f"todays winner is:{winner}")
list_prizes=['Rs10',"dairymilk","infomaths discount coupon"]
prize_won=random.choice(list_prizes)
#data to encode- this can be a secret message or a secret url
prize_data=f"Congratulations {winner} you have won {prize_won}!"

#create the qrcode object
qr=qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4
)
qr.add_data(prize_data)
qr.make(fit=True)
#create and save the image
img=qr.make_image(fill_color="black",back_color="white")
img.save(f"{winner}_prize_qr.png")
print("QR code generated successfully! check prize_qr.png for your prize details")