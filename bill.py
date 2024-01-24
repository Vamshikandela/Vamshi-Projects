from datetime import datetime
name=input("Enter Your Name:")
lists=''' 
Groceries of Household
Rice-35/kg
Bengal Gram-132/kg
Small chana-90/kg
Tide Detergent Powder-140/kg
Tide Liquid top load-155/litre
Tide Liquid front load-155/litre
Aerial Detergent Powder-130/kg
Aerial Liquid top load-140/litre
Aerial Liquid front load-140/litre
Santoor Aleovera soap (100gr)-140/4pcs
sugar-40/kg
salt-25/kg
freedom oil-120/pack
maggie-20/pack

'''
#print(lists)
#declaraton
price=0
qlist=[]
plist=[]
totalprice=0
ilist=[]
Finalprice=0
pricelist=[]
Total=[]
#rRate Declaration for items
items={"Rice":35,
       "Bengal Gram":132,
       "Small chana":90,
       "Tide Detergent Powder":140,
       "Tide Liquid top load":155,
       "Tide Liquid front load":155,
       "Aerial Detergent Powder":130,
       "Aerial Liquid top load":140,
       "Aerial Liquid front load":140,
       "Santoor Aleovera soap (100gr)":140/4,
       "sugar":40,
       "salt":25,
       "freedom oil":120,
       "maggie":20
}
#print(items)
option=int(input("for list of items press 1:"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if u want to buy press 1 or 2 to exit:"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your items:")
        quantity=int(input("Enter your Quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sorry you have entered item not avaliable in our store")
    else:
        print("you have entered a invalid key ..")
    inp=input("can i bill the items yes or no:") 
    if inp=="yes":
        pass
        if finalamount!=0:
            print(25*"=","VVSupermart",25*"=")
            print(28*"=","jagtial")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("sno",8*" ",'items',8*" ",'Quantity',3*" ",'price')
            for i in range(len(pricelist)):
                print(i,6*' ',6*' ',ilist[i],6*' ',qlist[i],6*' ',plist[i])
            print(75*"-") 
            print(50*" ",'TotalAmount:','Rs',totalprice) 
            print("gst amount",50*" ",'Rs',gst)
            
            print(75*"-")  
            
            
            if finalamount>=2000:
                Total=finalamount-100
                
            print(50*" ",'finalamount:','Rs',finalamount)  
            print(50*" ",'Totalamount:','Rs',Total)
            print(50*" ",'Thank for visting(Visit Again)')
            print(75*"-")
            print("Congrulations You have got  100 rs discount.....")
            break

        else:
            print(finalamount) 
            print(50*" ",'finalAmount:','Rs',finalamount)
               
            print(50*" ",'Thank for visting(Visit Again)')
        print("Shop more Than 2000 to get 100 rs discount.....")
            
                
         
             

 
