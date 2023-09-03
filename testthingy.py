import streamlit as st

st.set_page_config(page_title="Pizza Bakery", page_icon = ":pizza:")
st.title("Papa's Pizzeria (walmart version)")
st.subheader("Menu:pizza: || 1 Plain Pizza is 3 coins!")
st.write("For the toppings: ")
st.write("(1) Pepperoni costs 3 coins.")
st.write("(2) Olives cost 2 coins.")
st.write("(3) Double Cheese costs 4 coins.")
st.write("(4) Chicken costs 6 coins.")
st.write("(5) Pineapple costs 2 coins.")
st.write(":chicken: :cheese_wedge: :olive: :pineapple:")

number_of_pizzas  = st.number_input("How many pizzas do you want?")
if number_of_pizzas<0:
    st.write("You want...less than 1 pizza-? A negative pizza? STOP TORMENTING OUR WAITERS!")
if number_of_pizzas == 0:
    st.write("why are you even here?")
if number_of_pizzas>30:
    st.write("Oh...wow- thats a lot of pizzas.")

cost_per_pizza = 3

toppings = ["Pepperoni", "Olives", "Double Cheese", "Chicken", "Pineapple"]
toppingsprice = [3, 2, 4, 6, 2]


toppingschoice = st.number_input("Which topping would you like? Select from 1-5. If you do not want a topping, click 0.")

extracost = 0
if toppingschoice ==  1 :
    extracost = toppingsprice[0]
    st.write("yum. i like your taste. so basic but SO GOOD.")
if toppingschoice ==  2 :
    extracost = toppingsprice[1]
    st.write("underrated tbh.")
if toppingschoice ==  3 :
    extracost = toppingsprice[2]
    st.write("you are 5 years old.")
if toppingschoice == 4 :
    extracost = toppingsprice[3]
    st.write("lowkey my fav pizza is a good bbq chicken pizza ngl.")
if toppingschoice == 5 :
    extracost = toppingsprice[4]
    st.write("PINEAPPLE IS SUCH A GOOD TOPPING, I DONT CARE WHAT ANYONE SAYS, BY GOD I SWEAR THAT THE SWEET BALANCES OUT ESPECIALLY IF THERE- *nervous breakdown*")
if toppingschoice == 0:
    extracost = 0
if toppingschoice<0 or toppingschoice>5:
    st.write("Our waiter is very confused. Can you read? Please refresh, our waiter may ask for a raise :/")

if toppingschoice != 0:
    subtotal = number_of_pizzas * (cost_per_pizza * extracost)
    st.write("The cost before tax is: ", subtotal)
    tax_rate = 0.08
    sales_tax = subtotal * tax_rate
    total = subtotal + sales_tax
    st.write("The total cost is $", total)
    st.write("This includes ", subtotal, " coins for the food and  ", sales_tax, " coins in sales tax.")

if toppingschoice == 0:
    st.write("The cost before tax is: ", number_of_pizzas * cost_per_pizza)
    st.write("The total cost is ", (number_of_pizzas * cost_per_pizza)+ ((number_of_pizzas * cost_per_pizza) * 0.08))

    
