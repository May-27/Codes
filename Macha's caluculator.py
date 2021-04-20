print("welcome to Aggi petti matchaa calculator!!")
def go():
    resp = input("Continue ? Y/N ")
    if resp == "n" or resp == "N":
        return False
    return True
while True:
    print("Select operation,Operation em chesthavule kaani. kinda edho okati choose chesko.")
    print("1.ADD chey mawa")
    print("2.Poni SUBTRACT chey mawa")
    print("3.Vodhhule MULTIPLY chey")
    print("4.Muskoni DIVIDE chey")
    print("5.PERCENTAGE anna chey ra batta")   
    choice = input("RA RA BATTA EM CHESTHAVO CHEPPU(1/2/3/4/5):")

    num1 = int(input("Number nokku MAWA: "))
    num2 = int(input("Inko number nokki chudu : "))

    if choice == '1':
       print(num1,"+",num2,"=", ('Nee Answer mawa' ,num1 + num2))

    elif choice == '2':
       print(num1,"-",num2,"=", ('Nee Answer mawa' ,num1 - num2))

    elif choice == '3':
       print(num1,"*",num2,"=", ('Nee Answer mawa' ,num1 * num2))

    elif choice == '4':
       print(num1,"/",num2,"=", ('Nee Answer mawa' ,num1 / num2))
       
    elif choice == '5' :
        print(num1,"%",num2,"=", ('Nee Answer mawa' ,num1 % num2))
        
    else:
        print("Eedevadura eedu rey ,""SAKKANGGA NOKKU RA NA BATTA")
    if not go() :
          break
   
