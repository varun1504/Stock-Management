class Product:
    def GetProduct(self):
        self.__pid=input("Enter Product Id :")
        self.__pname=input("Enter Product Name :")
        self.__rate=int(input("Enter Product Rate :"))
        self.__stock=int(input("Enter Product Stock :"))
        return self.__pid
        print()
    def PutProduct(self):
        print("Product Id :",self.__pid,"\nProduct Name :",self.__pname,"\nProduct Rate :",self.__rate,"\nProduct Stock :",self.__stock)
        print()
    def Sale(self):
        qty=int(input("Enter quantity of Product you want :"))
        if(qty<=self.__stock):
            amt=qty*self.__rate
            self.__stock-=qty
            print("Amount :",amt)
            print()
        else:
            print("Less Stock..")
            print()
    def Purchase(self):
        qty=int(input("Enter quantity you want to purchase :"))
        self.__stock+=qty
        print()
PD=dict()   # PD(Product Details) is dictionary which will contain all products information.
n=int(input("Number of product you want :"))
for i in range(n):
    P=Product()
    key=P.GetProduct()
    print()
    PD.setdefault(key,P)   #setdefault(key,value) is a method of dictionary which insert key,value in dictionary.
#Now PD contains product id as a keys and object reference as a values
while(True):
    print("1] All Products \n2] Search Product \n3]Sale \n4]Purchase \n5] Exit\n")
    ch = input("Enter your choice :")
    if(ch=="1"):
        for p in PD.values():
            p.PutProduct()
            print()

    elif(ch=="2"):
        pid=input("Enter product Id you want to search :")
        P=PD.get(pid,"Not found...")  #get returns the value of key if found in dictionary otherwise will return message "Not found..."
        if(isinstance(P,Product)):
            P.PutProduct()
        else:
            print(P)

    elif(ch=="3"):
        pid=input("Enter product Id you want to search for sale :")
        P=PD.get(pid,"Not found...")
        if(isinstance(P,Product)):
            P.PutProduct()
            P.Sale()
        else:
            print(P)

    elif(ch=="4"):
        pid=input("Enter Product Id you want to search for purchase :")
        P=PD.get(pid,"Not Found...")
        if(isinstance(P,Product)):
            P.PutProduct()
            P.Purchase()
        else:
            print(P)

    elif(ch=="5"):
        print("GoodBye")
        break

    else:
        print("INVALID CHOICE\n")
