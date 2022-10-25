#List class, takes the objects and builds a cart list
class AddToCart(list):

    #Iterates through the list and returns items
    def search(self):
        final_list = []
        for x in self:
            final_list.append(x)
        return final_list

    #Calculates subtotal of cart
    def subtotal(self):
        stotal = 0
        for x in self:
            stotal += x.get_price()
        return stotal

    #Calculates tax amount of cart
    def tax(self, stotal):
        tax_amount = 3.25/100
        tax_applied = tax_amount * stotal
        return tax_applied

    #Calculates final total of cart
    def total(self,tax_applied,stotal):
        final_total = tax_applied + stotal
        return final_total

#Parent class, adds the burgers to the cart class
class SimpleBurger(object):
    cart = AddToCart()
    simple_burger_price = {'single': 7.99, 'double': 10.99}

    #Initializes simple burger instance variables
    def __init__(self,bun,patty):
        self.bun = bun
        self.patty = patty
        SimpleBurger.cart.append(self)

    #Returns price of burger according to patty type
    def get_price(self):
        return SimpleBurger.simple_burger_price[self.patty]

    #Returns string variables of burger contents
    def __str__(self):
        return str(self.bun) +"-"+ str(self.patty) +"-"+ str(SimpleBurger.simple_burger_price[self.patty])

#CheeseBurger subclass, child of SimpleBurger     
class CheeseBurger(SimpleBurger):
    cheese_type_price = {'american': 1.99, 'pepper jack': 0.99}

    #Initialize instance variables, inherit bun and patty from SimpleBurger class, add cheese instance variable
    def __init__(self,bun,patty,cheese):
        super().__init__(bun,patty)
        self.cheese = cheese

    #Returns price of burger according to cheese type
    def get_price(self):
        return (SimpleBurger.simple_burger_price[self.patty] + CheeseBurger.cheese_type_price[self.cheese])

    #Returns string variables of cheeseburger contents
    def __str__(self):
        return str(self.bun) +"-"+ str(self.patty) + " with " + str(self.cheese)  +"-"+ str(SimpleBurger.simple_burger_price[self.patty] + CheeseBurger.cheese_type_price[self.cheese])

#VeggieBurger subclass, child of SimpleBurger
class VeggieBurger(SimpleBurger):
    veggie_type_price = {'lettuce': 0.99, 'tomato': 0.99, 'caramelized onion': 2.99}

    #Initialize instance variables, inherit bun and patty from SimpleBurger class, add veggie instance variable
    def __init__(self,bun,patty,veggie):
        super().__init__(bun,patty)
        self.veggie = veggie
    #Returns price of burger according to veggie type
    def get_price(self):
        return (SimpleBurger.simple_burger_price[self.patty] + VeggieBurger.veggie_type_price[self.veggie])

    #Returns string variables of veggie burger contents
    def __str__(self):
        return str(self.bun) +"-"+ str(self.patty) + " with " + str(self.veggie) +"-"+ str(SimpleBurger.simple_burger_price[self.patty] + VeggieBurger.veggie_type_price[self.veggie])

#Main, charged with taking user input and producing output
def main():
    choice = ''
    print('******** Welcome to 209 Burger ******** \n\n')

    #Setting up user input loop to determine if they want to enter more burgers
    while choice!='no':
        burger_type = input('\tEnter type of Burger(simple/cheese/veggie): ')

        #If/elif loop to determine which type of burger the user is inputting
        if burger_type.lower() == 'simple':
            bun_type = input('\tEnter bun type (white/wheat): ')
            patty_type = input('\tEnter patty count (single/double): ')
            simple_object = SimpleBurger(bun_type,patty_type)
            choice = input("\tDo you want to continue ordering (yes/no): ")
        elif burger_type.lower() == 'cheese':
            bun_type = input('\tEnter bun type (white/wheat): ')
            patty_type = input('\tEnter patty count (single/double): ')
            cheese_type = input('\tEnter cheese type (american/pepper jack): ')
            cheese_object = CheeseBurger(bun_type,patty_type,cheese_type)
            choice = input("\tDo you want to continue ordering (yes/no): ")
        elif burger_type.lower() == 'veggie':
            bun_type = input('\tEnter bun type (white/wheat): ')
            patty_type = input('\tEnter patty count (single/double): ')
            veggie_type = input('\tEnter veggie type (lettuce/tomato/caramelized onion): ')
            veggie_object = VeggieBurger(bun_type,patty_type,veggie_type)
            choice = input("\tDo you want to continue ordering (yes/no): ")

    #Printing the receipt for the order
    print('\n\n\t******** Printing Receipt *******\n')
    counter = 1

    #Printing contents of AddToCart list class
    for x in SimpleBurger.cart.search():
        print("\t",counter,"-\t",x)
        counter+=1

    #Printing subtotal, tax, and final total
    subtotal = (SimpleBurger.cart.subtotal())
    tax = (SimpleBurger.cart.tax(subtotal))
    total = subtotal + tax
    print("\tSubtotal: ","{:.2f}".format(subtotal))
    print("\tTax: ","{:.2f}".format(tax))
    print("\tTotal: ","{:.2f}".format(total))
    print('\n\n******** Thanks for coming! *******\n')

main()
