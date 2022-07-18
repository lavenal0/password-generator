def generator():
    import random
    a=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    b=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    c=[1,2,3,4,5,6,7,8,9,0]
    s=['!','@','#','$']
    print("---------------------------------------------------------")
    c2=int(input("Enter Length of Password : "))
    d=[random.choice(s),random.choice(b),random.choice(c),random.choice(a),random.choice(b),random.choice(s),random.choice(s),random.choice(a),random.choice(c),random.choice(a),random.choice(b),random.choice(c),random.choice(a),random.choice(b),random.choice(c)]
    random.shuffle(d)
    print("---------------------------------------------------------")
    if c2==15:
        print("Password Generated = ",d[0],d[1],d[2],d[3],d[4],d[5],d[6],d[7],d[8],d[9],d[10],d[11],d[12],d[13],d[14])
    elif c2==14:
        print("Password Generated = ",d[0],d[1],d[2],d[3],d[4],d[5],d[6],d[7],d[8],d[9],d[10],d[11],d[12],d[13])
    elif c2==13:
        print("Password Generated = ",d[0],d[1],d[2],d[3],d[4],d[5],d[6],d[7],d[8],d[9],d[10],d[11],d[12])
    elif c2==12:
        print("Password Generated = ",d[0],d[1],d[2],d[3],d[4],d[5],d[6],d[7],d[8],d[9],d[10],d[11])
    elif c2==11:
        print("Password Generated = ",d[0],d[1],d[2],d[3],d[4],d[5],d[6],d[7],d[8],d[9],d[10])
    elif c2==10:
        print("Password Generated = ",d[0],d[1],d[2],d[3],d[4],d[5],d[6],d[7],d[8],d[9])
    elif c2==9:
        print("Password Generated = ",d[0],d[1],d[2],d[3],d[4],d[5],d[6],d[7],d[8])
    elif c2==8:
        print("Password Generated = ",d[0],d[1],d[2],d[3],d[4],d[5],d[6],d[7])
    elif c2==7:
        print("Password Generated = ",d[0],d[1],d[2],d[3],d[4],d[5],d[6])
    elif c2==6:
        print("Password Generated = ",d[0],d[1],d[2],d[3],d[4],d[5])
    elif c2==5:
        print("Password Generated = ",d[0],d[1],d[2],d[3],d[4])
    elif c2==4:
        print("Password Generated = ",d[0],d[1],d[2],d[3])
    elif c2==3:
        print("Password Generated = ",d[0],d[1],d[2])
    elif c2<=2:
        print("Password couldn't Generated Password Length is too Short")
    else:
        print("Password couldn't Generated Because it is too lengthy")
    print("---------------------------------------------------------")
    print("1.Continue\n2.Back\n3.Exit")
    print("---------------------------------------------------------")
    x=int(input("Enter your choice : "))
    print("---------------------------------------------------------")
    if x==1:
        generator()
    elif x==2:
        password()
    elif x==3:
        exit()
    else:
        print("Invalid input")
        rndm()
    
def password():
    import random
    print("---------------------------------------------------------")
    print("1.Password Generator\n2.Exit")
    print("---------------------------------------------------------")
    y = int(input("Enter your Choice : "))
    if y == 1:
        generator()
    elif y == 2:
        exit()
    else :
        print("---------------------------------------------------------")
        print("Invalid input")
        print("---------------------------------------------------------")
        rndm()
password()
