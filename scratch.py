#to keep track of how long it's been since the user wore an item, etc.
from datetime import datetime

#types of clothing will be sorted into the following dictionaries:

top = {}
bottom = {}
both = {}
shoe = {}
accessory = {}

#the next 5 functions keep track of how many times each item has been worn and when was last worn by adding one to
#the count & updating the time to the time the item is selected as worn by using the now function from datetime. Both
#these pieces of info are kept as values to keys to one of the dictionaries within the proper dictionary

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

#eventually there will be a stats function for each of the sub-closets,
#But I've only gotten as far as to make one to see if I can get it to work

def top_stats(key):
    print("Worn",top[key]['Times_Worn'],"times.")
    print("Last worn on", top[key]['Last_Time_Worn'])

#Each item type is a separate dictionary. Within that dictionary each item is it's own dictionary with the values
# containing the different pieces of the item name and the count of how many types it's been worn, when it
#was first worn, and when it was last worn. The following function sets up a unique name for each item dictionary/key
#within the type dictionary & adds the item dictionary/key to the type dictionary

def newitem():
    now = datetime.now()
    webster= input("Is this item a top, bottom, both(i.e. dress or jumper), accessory, or shoes?\n").lower()
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

#the next function allows a user to pick what they're going to wear. input should be a number, not words.
#you can look at all the clothing items at once or by type
# the list becomes visible for the user to select an item.
# that numerical selection is then used to index their item out of the list.


def openCloset():
    choice2=input("\n1. Tops\n2. Bottoms\n3. Both(ie dress or jumper)\n 4. Shoes\n5. Accessories\n6. Full Closet\n7. Done\n")
    def fullCloset():
        topList= []
        toplistNumber= 0
        print("TOPS")
        for item in top.keys():
            topList.append(item)
            print(toplistNumber,'. ',item,)
            toplistNumber+=1
        print("\n")
        bottomList= []
        bottomlistNumber= 0
        print("BOTTOMS")
        for item in bottom.keys():
            bottomList.append(item)
            print(bottomlistNumber,'. ',item)
            bottomlistNumber+=1
        print("""\n""")
        bothList= []
        bothlistNumber= 0
        print("""BOTH (ie dresses, jumpers, etc.)""")
        for item in both.keys():
            bothList.append(item)
            print(bothlistNumber,'. ',item)
            bothlistNumber+=1
        print("\n")
        shoeList= []
        shoelistNumber= 0
        print("SHOES")
        for item in shoe.keys():
            shoeList.append(item)
            print(shoelistNumber,'. ',item)
            shoelistNumber+=1
        print("\n")
        accessoryList= []
        accessorylistNumber= 0
        print("ACCESSORIES")
        for item in accessory.keys():
            accessoryList.append(item)
            print(accessorylistNumber,'. ',item)
            accessorylistNumber+=1
        print("\n")
        toWear=input("""Found something you'd like to wear?\n1.Yes\n2. No""")
        if toWear=='1':
            toWearType= input("What type of item is it?").lower()
            print("\n1. Top\n2. Bottom\n3. Both\n4.Accessory\n5.Shoes")
            if toWearType=='top' or ' top':
                choice3=int(input("Wear Top Number:\n"))
                choice4=topList[choice3]
                top_worn(choice4)
            elif toWearType=='bottom' or ' bottom' or 'bottoms':
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
        if toWear== '2':
            menu()
        else:
            fullCloset()
    if choice2== '6':
        fullCloset()
    elif choice2== '1':
        print("TOPS")
        topList= []
        listNumber= 0
        for item in top.keys():
            topList.append(item)
            print(listNumber,'. ',item)
            listNumber+=1
            print(top_stats(item))
        toWear=input("""Found something you'd like to wear?\n 1.Yes \2. No\n""")
        if toWear=='1':
            choice3=int(input("Wear Top Number:\n"))
            choice4=topList[choice3]
            top_worn(choice4)
            openCloset()
        else:
            openCloset()
    elif choice2=='2':
        print("BOTTOMS")
        bottomList= []
        listNumber= 0
        for item in bottom.keys():
            bottomList.append(item)
            print(listNumber,'. ',item)
            listNumber+=1
        toWear=input("""Found something you'd like to wear?\n1.Yes\n2. No\n""")
        if toWear=='1':
            choice3=int(input("Wear Bottom Number:\n"))
            choice4=bottomList[choice3]
            bottom_worn(choice4)
            openCloset()
        else:
            openCloset()
    elif choice2=='3':
        bothList= []
        listNumber= 0
        print("BOTH")
        for item in both.keys():
            bothList.append(item)
            print(listNumber,'. ',item)
            listNumber+=1
        toWear=input("""Found something you'd like to wear?\n1.Yes\n2. No\n""")
        if toWear=='1':
            choice3=int(input("Wear Both Number:\n"))
            choice4=bothList[choice3]
            both_worn(choice4)
            openCloset()
        else:
            openCloset()
    elif choice2=='4':
        print("SHOES")
        shoeList= []
        listNumber= 0
        for item in shoe.keys():
            shoeList.append(item)
            print(listNumber,'. ',item)
            listNumber+=1
        toWear=input("""Found something you'd like to wear?\n1.Yes\n2. No\n""")
        if toWear=='1':
            choice3=int(input("Wear Shoes Number:\n"))
            choice4=shoeList[choice3]
            shoe_worn(choice4)
            openCloset()
            print(shoe)
        else:
            openCloset()
    elif choice2=='5':
        print("ACCESSORIES")
        accessoryList= []
        listNumber= 0
        for item in accessory.keys():
            accessoryList.append(item)
            print(listNumber,'. ',item)
            listNumber+=1
        toWear=input("""Found something you'd like to wear?\n1.Yes\n2. No\n""")
        if toWear=='1':
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
# This is the main menu to which you should always navigate back. It will let you pick your own outfit,
# get a recommendation, or add another item to the dictionaries. Or rather, it lets you navigate to the
#functions that do these things


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

#now that the functions have been created, we can actually use them. the program visibly starts running here.
# it starts you off by making you put some items in the dictionaries of your closet so that you can later manipulate them.

print("""Fill your moth closet.""")
newitem()
intro()
