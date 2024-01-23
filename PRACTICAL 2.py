fh=open('prac2.txt','w')
Choice = int(input("""Select 1.For Area of Rectangle 
                   2. For Perimeter of rectangle     :  """))
if Choice == 1 :
    len = int(input("Enter the length of Rectangle :"))
    bre = int(input("Enter the Breadth o Rectangle :"))
    Area = len * bre
    fh.write(str(Area))
elif Choice == 2 :
    length = int(input("Enter the length of Rectangle :"))
    breadth = int(input("Enter the Breadth o Rectangle :"))
    Perimeter = 2 *( length + breadth)
    fh.write(str(Perimeter))
else :
    print( )
    fh.close()
    