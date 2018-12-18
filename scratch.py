from datetime import datetime

top = {}
bottom = {}
both = {}
shoe = {}
accessory = {}


def top_worn(key):
    now = datetime.now()
    top[key]['Times_Worn']+= 1
    top[key]['Last_Time_Worn']=now

def bottom_worn(key):
    now = datetime.now()
    bottom[key]['Times_Worn']+= 1
    bottom[key]['Last_Time_Worn']=now

def both_worn(key):
    now = datetime.now()
    both[key]['Times_Worn']+= 1
    both[key]['Last_Time_Worn']=now

def shoe_worn(key):
    now = datetime.now()
    shoe[key]['Times_Worn']+=1
    shoe[key]['Last_Time_Worn']=now

def accessory_worn(key):
    now = datetime.now()
    accessory[key]['Times_Worn']+=1
    accessory[key]['Last_Time_Worn']=now



def newitem():
    now = datetime.now()
    webster= input("Is it a top, bottom, both(i.e. dress or jumper), accessory, or pair of shoes?\n").lower()
    if webster == 'top' or webster == ' top':
        piece0= input('Type of top:')
        piece1 = input('Brand:')
        piece2 = input('Style:')
        piece3 = input('Color:')
        piece4 = input('Other descriptor:')
        new_item_key = piece3 +" "+ piece4+" " + piece2 +" "+piece1+" "+piece0
        new_item= {'Brand':piece1,'Style':piece2,'color':piece3, 'other':piece4,'Times_Worn':0,
                   'Last_Time_Worn':now,'First_Time_Worn':now}
        top[new_item_key]= new_item
    elif webster == 'bottom' or webster == ' bottom':
        piece0= input('Type of bottom:')
        piece1 = input('Brand:')
        piece2 = input('Style:')
        piece3 = input('Color:')
        piece4 = input('Other descriptor:')
        new_item_key = piece3 +" "+ piece4+" " + piece2 +" "+piece1+" "+piece0
        new_item= {'Brand':piece1,'Style':piece2,'color':piece3, 'other':piece4,'Times_Worn':0,'Last_Time_Worn':now,'First_Time_Worn':now}
        bottom[new_item_key]= new_item
    elif webster == 'both' or webster == ' both':
        piece0= input('Type of item:')
        piece1 = input('Brand:')
        piece2 = input('Style:')
        piece3 = input('Color:')
        piece4 = input('Other descriptor:')
        new_item_key = piece3 +" "+ piece4+" " + piece2 +" "+piece1+" "+piece0
        new_item= {'Brand':piece1,'Style':piece2,'color':piece3, 'other':piece4,'Times_Worn':0,'Last_Time_Worn':now,'First_Time_Worn':now}
        both[new_item_key]= new_item
    elif webster == 'accessory' or webster == ' accessory':
        piece0= input('Type of accessory:')
        piece1 = input('Brand:')
        piece2 = input('Style:')
        piece3 = input('Color:')
        piece4 = input('Other descriptor:')
        new_item_key = piece3 +" "+ piece4+" " + piece2 +" "+piece1+" "+piece0
        new_item= {'Brand':piece1,'Style':piece2,'color':piece3, 'other':piece4,'Times_Worn':0,'Last_Time_Worn':now,'First_Time_Worn':now}
        accessory[new_item_key]= new_item
    elif webster == 'pair of shoes' or webster=='shoes' or webster ==' shoes' or webster == ' pair of shoes':
        piece0= input('Type of shoes:')
        piece1 = input('Brand:')
        piece2 = input('Style:')
        piece3 = input('Color:')
        piece4 = input('Other descriptor:')
        new_item_key = piece3 +" "+ piece4+" " + piece2 +" "+piece1+" "+piece0
        new_item= {'Brand':piece1,'Style':piece2,'color':piece3, 'other':piece4,'Times_Worn':0,'Last_Time_Worn':now,'First_Time_Worn':now}
        shoe[new_item_key]= new_item
    else:
        print('Moth does not recognize your answer. Please check your spelling and try again.')
        newitem()

#skeleton=newitem()
#print(accessory_worn(skeleton))
#print(accessory)

def openCloset():
    choice2=input("\n1. Tops\n2. Bottoms\n3. Both(ie dress or jumper)\n 4. Shoes\n5. Accessories\n6. Full Closet\n7. Done\n")
    def fullCloset():
        topList= []
        toplistNumber= 0
        for item in top.keys():
            topList.append(item)
            print(toplistNumber,'. ',item)
            toplistNumber+=1
        bottomList= []
        bottomlistNumber= 0
        for item in bottom.keys():
            bottomList.append(item)
            print(bottomlistNumber,'. ',item)
            bottomlistNumber+=1
        bothList= []
        bothlistNumber= 0
        for item in top.keys():
            bothList.append(item)
            print(bothlistNumber,'. ',item)
            bothlistNumber+=1
        shoeList= []
        shoelistNumber= 0
        for item in top.keys():
            shoeList.append(item)
            print(shoelistNumber,'. ',item)
            shoelistNumber+=1
        accessoryList= []
        accessorylistNumber= 0
        for item in top.keys():
            accessoryList.append(item)
            print(accessorylistNumber,'. ',item)
            accessorylistNumber+=1
        toWear=input("""Found something you'd like to wear?\n1.Yes\2. No""")
        if toWear==1
            toWearType= input("What type of item is it?").lower()
            if toWearType=='top' or ' top':
                choice3=int(input("Wear Top Number:\n"))
                choice4=topList[choice3]
                top_worn(choice4)
            elif toWearType=='bottom' or ' bottom':
                choice3=int(input("Wear Bottom Number:\n"))
                choice4=bottomList[choice3]
                bottom_worn(choice4)
            elif toWearType=='both' or ' both':
                choice3=int(input("Wear Both Number:\n"))
                choice4=bothList[choice3]
                both_worn(choice4)
            elif toWearType=='accessory' or ' accessory':
                choice3=int(input("Wear Accessory Number:\n"))
                choice4=bottomList[choice3]
                accessory_worn(choice4)
            elif toWearType=='shoe' or ' shoes' or ' shoe' or 'shoes' or 'pair of shoes' or ' pair of shoes':
                choice3=int(input("Wear Bottom Number:\n"))
                choice4=bottomList[choice3]
                bottom_worn(choice4)
            else:
            print("Moth does not recognize your selection. Please check your spelling and try again.")
            fullCloset()
        if toWear== 2:
            menu()
        else:
            fullCloset()
    if choice2== '6':
        fullCloset()
    elif choice2== '1':
        topList= []
        listNumber= 0
        for item in top.keys():
            topList.append(item)
            print(listNumber,'. ',item)
            listNumber+=1
        toWear=input("""Found something you'd like to wear?\n1.Yes\2. No""")
        if toWear==1:
            choice3=int(input("Wear Item Number:\n"))
            choice4=topList[choice3]
            top_worn(choice4)
            openCloset()
        else:
            openCloset()
    elif choice2=='2':
        bottomList= []
        listNumber= 0
        for item in bottom.keys():
            bottomList.append(item)
            print(listNumber,'. ',item)
            listNumber+=1
        toWear=input("""Found something you'd like to wear?\n1.Yes\2. No""")
        if toWear==1:
            choice3=int(input("Wear Item Number:\n"))
            choice4=bottomList[choice3]
            bottom_worn(choice4)
            openCloset()
        else:
            openCloset()
    elif choice2=='3':
        bothList= []
        listNumber= 0
        for item in top.keys():
            bothList.append(item)
            print(listNumber,'. ',item)
            listNumber+=1
        toWear=input("""Found something you'd like to wear?\n1.Yes\2. No""")
        if toWear==1:
            choice3=int(input("Wear Item Number:\n"))
            choice4=bothList[choice3]
            both_worn(choice4)
            openCloset()
        else:
            openCloset()
    elif choice2=='4':
        shoeList= []
        listNumber= 0
        for item in top.keys():
            shoeList.append(item)
            print(listNumber,'. ',item)
            listNumber+=1
        toWear=input("""Found something you'd like to wear?\n1.Yes\2. No""")
        if toWear==1:
            choice3=int(input("Wear Item Number:\n"))
            choice4=shoeList[choice3]
            shoe_worn(choice4)
            openCloset()
        else:
            openCloset()
    elif choice2=='5':
        accessoryList= []
        listNumber= 0
        for item in top.keys():
            accessoryList.append(item)
            print(listNumber,'. ',item)
            listNumber+=1
        toWear=input("""Found something you'd like to wear?\n1.Yes\2. No""")
        if toWear==1:
            choice3=int(input("Wear Item Number:\n"))
            choice4=accessoryList[choice3]
            accessory_worn(choice4)
        else:
            openCloset()
        openCloset()
    elif choice2== '7':
        print()
    else:
        openCloset()

#def recommend():

def menu():

    choice = input("1. Choose an outfit\n2. Just tell me what to wear\n3. Add another item to my closet\n")
    if choice == '1':
        openCloset()
        menu()
    elif choice =='3':
        newitem()
        menu()
    else:
        menu()
 #   elif choice =='2':
  #      recommend()




def intro():
    first_choice=input("""1. Add another item\n2. My closet is full enough. Let's get dressed.\n""")
    if first_choice=='1':
        newitem()
        intro()
    elif first_choice=='2':
        menu()
    else:
        intro()

print("""Fill your Moth closet""")
newitem()
intro()
