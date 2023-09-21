import streamlit as st

#page config


st.set_page_config(page_title="Pizza Bakery", page_icon = ":pizza:")
st.title("Papa's Pizzeria - Walmart Edition")
st.header("Menu || Plain Pizzas cost 3 coins.")
st.subheader("Toppings")
st.subheader(":chicken: :cheese_wedge: :olive: :pineapple: :pizza:")
st.write("(1) Pepperoni costs 3 coins.")
st.write("(2) Olives cost 2 coins.")
st.write("(3) Double Cheese costs 4 coins.")
st.write("(4) Chicken costs 6 coins.")
st.write("(5) Pineapple costs 2 coins.")
st.header("Place Your Order")

#base pizza
number_of_pizzas  = st.number_input("How many pizzas do you want?")
if number_of_pizzas<0:
    st.write("You want...less than 1 pizza-? A negative pizza? STOP TORMENTING OUR WAITERS!")
    fornow1 = 0
    fornow2 = 0
    fornow3 = 0
    fornow4 = 0
if number_of_pizzas == 0:
    st.write("why are you even here?")
if number_of_pizzas>30:
    st.write("Oh...wow- thats a lot of pizzas.")

cost_per_pizza = 3

#toppings
toppings = ["Pepperoni", "Olives", "Double Cheese", "Chicken", "Pineapple"]
toppingsprice = [3, 2, 4, 6, 2]

toppingschoice = st.number_input("Would you like a topping? If so, select from 1-5. If you do not want a topping, proceed to the bill.")

extracost = 0
if toppingschoice ==  1 :
    extracost = toppingsprice[0]
    st.write("valley girl in the restaurant: its okay to be basic, i literally could never though.")
if toppingschoice ==  2 :
    extracost = toppingsprice[1]
    st.write("college student waiter: underrated tbh.")
if toppingschoice ==  3 :
    extracost = toppingsprice[2]
    st.write("judgy teenager in the restaurant: you are 5 years old.")
if toppingschoice == 4 :
    extracost = toppingsprice[3]
    st.write("14 year old boy in the restaurant: lowkey my fav pizza is a good bbq chicken pizza ngl.")
if toppingschoice == 5 :
    extracost = toppingsprice[4]
    st.write("hippie waiter: PINEAPPLE IS SUCH A GOOD TOPPING, I DONT CARE WHAT ANYONE SAYS, BYGODISWEARTHATTHESWEETMAKESTHESAVOUR- *nervous breakdown*")
if toppingschoice == 0:
    extracost = 0
if toppingschoice != 0 and toppingschoice != 1 and toppingschoice != 2 and toppingschoice != 3 and toppingschoice != 4 and toppingschoice != 5:
     st.write("Our waiter is very confused. Can you read?")

#bill

if number_of_pizzas!=0:
    if toppingschoice ==  0 and number_of_pizzas == 1:
        st.write(number_of_pizzas, " Margherita Pizza coming right up!...")
    if toppingschoice ==  1 and number_of_pizzas == 1:
        st.write(number_of_pizzas, " Pepperoni Pizza coming right up!...")
    if toppingschoice ==  2 and number_of_pizzas == 1:
        st.write(number_of_pizzas, " Olive-Topped Pizza coming right up!...")
    if toppingschoice ==  3 and number_of_pizzas == 1:
        st.write(number_of_pizzas, " Double-Cheese Pizza coming right up!...")
    if toppingschoice ==  4 and number_of_pizzas == 1:
        st.write(number_of_pizzas, " Barbeque Chicken Pizza coming right up!...")
    if toppingschoice ==  5 and number_of_pizzas == 1:
        st.write(number_of_pizzas, " Pineapple Pizza coming right up!...")

    if toppingschoice ==  0 and number_of_pizzas>1:
        st.write(number_of_pizzas, " Margherita Pizzas coming right up!...")
    if toppingschoice ==  1 and number_of_pizzas>1:
        st.write(number_of_pizzas, " Pepperoni Pizzas coming right up!...")
    if toppingschoice ==  2 and number_of_pizzas>1:
         st.write(number_of_pizzas, " Olive-Topped Pizzas coming right up!...")
    if toppingschoice ==  3 and number_of_pizzas>1:
        st.write(number_of_pizzas, " Double-Cheese Pizzas coming right up!...")
    if toppingschoice ==  4 and number_of_pizzas>1:
        st.write(number_of_pizzas, " Barbeque Chicken Pizzas coming right up!...")
    if toppingschoice ==  5 and number_of_pizzas>1:
        st.write(number_of_pizzas, " Pineapple Pizzas coming right up!...")

    st.subheader("Your Bill :money_with_wings:")
    st.write("--->Base Pizza Price: 3")
    if toppingschoice == 1:
        st.write("--->Topping: Pepperoni, Price: 3")
    if toppingschoice == 2:
        st.write("--->Topping: Olives, Price: 2")
    if toppingschoice == 3:
        st.write("--->Topping: Double Cheese, Price: 4")
    if toppingschoice == 4:
        st.write("--->Topping: Chicken, Price: 6")
    if toppingschoice == 5:
        st.write("--->Topping: Pineapple, Price: 2")
    if toppingschoice == 0:
        st.write("--->Topping: N/A, Price: N/A")
    
    if toppingschoice!=0:
        st.write("--->Total Base Price: ", cost_per_pizza + extracost)
        st.write("--->Quantity: ", number_of_pizzas)

    if toppingschoice != 0:
        subtotal = number_of_pizzas * (cost_per_pizza + extracost)
        st.write("Subtotal: ", subtotal)
        tax_rate = 0.08
        sales_tax = subtotal * tax_rate
        total = subtotal + sales_tax
        fornow3 =  st.write("Total (including tax): ", total)
        fornow4 = st.write("This includes ", subtotal, " coins for the food and  ", sales_tax, " coins in sales tax.")

    if toppingschoice == 0:
        fornow1 = st.write("The cost before tax is: ", number_of_pizzas * cost_per_pizza)
        fornow2 = st.write("The total cost is ", (number_of_pizzas * cost_per_pizza)+ ((number_of_pizzas * cost_per_pizza) * 0.08))

    
