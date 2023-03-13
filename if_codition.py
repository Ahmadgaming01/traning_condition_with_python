
# normal condition
x = 5
if x > 6:
    print ('Welcome')
else :
    print ('not correct')

# condition with more elif
        
x = 100
if x > 200:
    print ('x>200')
elif x > 300:
    print ('x>300')
elif x > 400:
    print ('x != 400')
else :
    print (x)

#condition in ander condition
    
x = 500
if x > 600:
    print ('you code not correct')
    if x > 400:
        print ('you have benn login')
    elif x != 500:
            print ('plese try agin ! ')
    else :
            print ('you cant login more ')
elif x == 500:
        print ('done')
else :
    print ('go out ')

# condition in one line

x = 150
print ('Welcome') if x > 200 else print ('x != 200')


#condiition with in and not in

x = [1,2,3,4,5]
if 5 in x :
    print ('yes')
    if 5 not in x :
        print ('right !')
    else :
        print ('false')

else : ('false ' )

#Condition with all and any

x = 5
y = 7
z = 10

if x == 5 and y == 7 and z == 10:
    print ('right ')

if all ([x== 5 , y== 7 , z== 10]):
    print ('ok')

if any ([x== 5 , y== 7 , z == 10]):
    print ('meby')
    


