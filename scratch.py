top = {}
bottom = {}
both = {}
shoe = {}
accessory = {}

#'pair of shoes'='shoes'

number_times_worn= 0
#def reccomend():

def top_worn(key):
    top[key]+= 1
    return top[key]

def bottom_worn(key):
    bottom[key]+= 1
    return bottom[key]

def both_worn(key):
    both[key]+= 1
    return both[key]

def shoe_worn(key):
    shoe[key]+=1
    return shoe[key]

def accessory_worn(key):
    accessory[key]+=1
    return accessory[key]



def newitem():
    webster= input("Is it a top, bottom, both(i.e. dress or jumper), accessory, or pair of shoes?").lower()
    if webster == 'top':
        piece0= input('Type of top:')
        piece1 = input('Brand:')
        piece2 = input('Style:')
        piece3 = input('Color:')
        piece4 = input('Other descriptor:')
        new_item = piece3 +" "+ piece4+" " + piece2 +" "+piece1+" "+piece0
        top[new_item]= 0
    elif webster == 'bottom':
        piece0= input('Type of bottom:')
        piece1 = input('Brand:')
        piece2 = input('Style:')
        piece3 = input('Color:')
        piece4 = input('Other descriptor:')
        new_item = piece3 +" "+ piece4+" " + piece2 +" "+piece1+" "+piece0
        bottom[new_item]= 0
    elif webster == 'both':
        piece0= input('Type of item:')
        piece1 = input('Brand:')
        piece2 = input('Style:')
        piece3 = input('Color:')
        piece4 = input('Other descriptor:')
        new_item = piece3 +" "+ piece4+" " + piece2 +" "+piece1+" "+piece0
        both[new_item]= 0
    elif webster == 'accessory':
        piece0= input('Type of accessory:')
        piece1 = input('Brand:')
        piece2 = input('Style:')
        piece3 = input('Color:')
        piece4 = input('Other descriptor:')
        new_item = piece3 +" "+ piece4+" " + piece2 +" "+piece1+" "+piece0
        accessory[new_item]= 0
    elif webster == 'pair of shoes' or webster=='shoes':
        piece0= input('Type of shoes:')
        piece1 = input('Brand:')
        piece2 = input('Style:')
        piece3 = input('Color:')
        piece4 = input('Other descriptor:')
        new_item = piece3 +" "+ piece4+" " + piece2 +" "+piece1+" "+piece0
        shoe[new_item]= 0
    else:
        print('Moth does not recognize your answer. Pleas check your spelling and try again.')
    return new_item

skeleton=newitem()
#print(accessory_worn(skeleton))
print(skeleton)
