def solution():
    """At the burger hut, you can buy a burger for $5, french fries for $3, and a soft drink for $3.  If you order a special burger meal, you get all 3 of these food items for $9.50. A kid's burger is $3, a kid's french fries are $2, and a kid's juice box is $2.  They also have a kids meal of all 3 kids' food items for $5. Mr. Parker buys 2 burger meals for his wife and himself.  He also buys 2 burger meals and 2 kid's meals for his 4 children.  How much money does Mr. Parker save by buying the 6 meals versus buying the individual food items?"""
    # Define the prices of individual food items and meal deals
    BURGER_PRICE = 5
    FRIES_PRICE = 3
    DRINK_PRICE = 3
    KID_BURGER_PRICE = 3
    KID_FRIES_PRICE = 2
    JUICE_PRICE = 2
    BURGER_MEAL_PRICE = 9.5
    KID_MEAL_PRICE = 5

    # Calculate the cost of buying individual food items
    individual_cost = (2 * BURGER_PRICE) + (2 * BURGER_PRICE) + (4 * KID_BURGER_PRICE) + (4 * KID_FRIES_PRICE) + (4 * JUICE_PRICE)

    # Calculate the cost of buying meal deals
    meal_cost = (2 * BURGER_MEAL_PRICE) + (2 * KID_MEAL_PRICE)

    # Calculate the amount saved by buying meal deals instead of individual food items
    savings = individual_cost - meal_cost

    # Display the amount saved
    result = savings
    return result

print(solution())