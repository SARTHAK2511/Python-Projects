#health Managment System
from matplotlib.pyplot import flag


def gettime():
    import datetime
    return datetime.datetime.now()

def Write_Food(name1):
    Flag = True
    while Flag:
        fileName=name1+'_food' + '.txt'
        f=open(fileName,'a+')
        Entry = str(input(" \n Enter the food item or Enter E to exit \n "))
        if Entry == 'E' or Entry=='e':
            Flag=False
            break
        else:
            Final=str(gettime())+" "+Entry+" "
            f.write(Final+"\n")
            print("Entry added \n")
            f.close()
def Write_Exercise(name1):
    Flag = True
    while Flag:
        fileName=name1+'_Exercise'+ '.txt'
        f=open(fileName,'a+')
        Entry = input(" \n Enter the Exercise done or Enter E to exit \n ")
        if Entry == 'E' or Entry=='e':
            Flag=False
            break
        else:
            Final=str(gettime())+" "+Entry
            f.write(Final)
            print("Entry added \n")
            f.close()
def GetFood(name1):
    fileName=name1+'_food' + '.txt'
    f=open(fileName,'r')
    print(f.readlines())
    f.close()
    return
def GetExercise(name1):
    fileName=name1+'_Exercise' + '.txt'
    f=open(fileName,'r')
    print(f.readlines())
    f.close()
    return

Flag1=True
while Flag1:

    print(" \n Welcome to Health Managment System , Choose the action you want to perform ")
    print( '''
    1: Enter Users Food Data 
    2: Enter  Users Exercise Data
    3: Get User Food Data
    4: Get User Exercise Data
    5: Exit \n'''  )
    a=int(input())
    if a==1:
        name=input("Enter user name \n")
        Write_Food(name)
    if a==2:
        name=input("Enter user name\n")
        Write_Exercise(name)
    if a==3:
        name=input("Enter user name \n")
        GetFood(name)
    if a==4:
        name=input("Enter user name \n")
        GetExercise(name)
    if a==5:
        Flag1= False
    else:
        print(" \n Enter valid input \n")