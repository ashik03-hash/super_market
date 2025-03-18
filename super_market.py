import requests
import smtplib
url=" http://demo7446238.mockable.io/supermarket_datas"
response=requests.get(url)
print(response.status_code)

def super_market_bill():
   if response.status_code==200:
      get_data=response.json()
      price=get_data["Fruit_Price"]
      fruit=get_data["Fruit"]
      cust_mail=get_data["Mail_id"]
      cust=input("Enter the fruit you want to buy :")
      if cust in fruit:
         print(f"Hi! {fruit} is available select the quantity you want ")
      else:
         print("sorry the fruit you have selected is not available")
   
      Quantity=int(input("Enter the quantity of fruit you want :"))
      total=int(price)*Quantity
      print(f"You have selected {cust} and the Quantity is {Quantity}")
      bill_choice=input("Hi Sir you want the bill in your mail or Hard copy :")
      if bill_choice == "mail":
         sender_mail="mashikashi03@gmail.com"
         s=smtplib.SMTP('smtp.gmail.com',587)
         s.starttls()
         s.login(sender_mail,"qrbo yxef izlq hdwp")
         message=f"Hi! Thank you for purchasing your bill amount is{total}" 
         s.sendmail(sender_mail,cust_mail,message)
         s.quit()
         print("The mail have been sended successfully please check your inbox....")
      elif bill_choice == "hard copy":
         f=open("cust_bill.txt","r")
         
         print(f.read())
         f.close()
      else:
         print("Please select a valid Bill option")
         



   else:
      print("API is not activated")

super_market_bill()