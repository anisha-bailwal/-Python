from captcha.image import ImageCaptcha
import random
import string
char=string.ascii_letters + string.digits+string.ascii_lowercase
cp="".join(random.sample(char,6))
print(cp)
image=ImageCaptcha(width=350,height=150)
captcha_text=cp
image.write(captcha_text,'captcha.png')
print("Captcha image generated and saved as 'captcha.png'")