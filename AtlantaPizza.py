# AtlantaPizza.py - a simple pizza cost calculator

#Number of Pizzas
number_of_pizzas = eval(input("how many pizzas do you want? "))

#Menu Cost
cost_per_pizza = eval(input("how much does each pizza cost? "))

#Subtotal
subtotal = number_of_pizzas * cost_per_pizza

#Sales Tax @ 8% of the subtotal 
tax_rate = 0.08
sales_tax = subtotal * tax_rate

#Final Total
total = subtotal + sales_tax


#Total Due from Customer
print("The total cost is $",total)
print("This includes $", subtotal, "for the pizza and")
print("$", sales_tax, "in sales tax.")
