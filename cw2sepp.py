def my_name():
    print ("my name is Retaj") 

my_name()



def my_meal (food , drink) :
    print (" i like to eat {food} and while drink {drink}")

my_meal("pasta" , "coffee")

def cube(number) :
    return number**3
print(cube(7))
def by_three (number) :
    if number%3 ==0 : 
        return cube(number)
    else:
        return False
    print(by_three (2))