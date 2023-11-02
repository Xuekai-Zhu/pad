def solution():
    """At the burger hut, you can buy a burger for $5, french fries for $3, and a soft drink for $3. If you order a special burger meal, you get all 3 of these food items for $9.50. A kid’s burger is $3, a kid’s french fries are $2, and a kid's juice box is $2. They also have a kids meal of all 3 kids' food items for $5. Mr. Parker buys 2 burger meals for his wife and himself. He also buys 2 burger meals and 2 kid's meals for his 4 children. How much money does Mr. Parker save by buying the 6 meals versus buying the individual food items?"""
    # Define the individual prices of the food items
    burger_price = 5
    fries_price = 3
    drink_price = 3
    kids_burger_price = 3
    kids_fries_price = 2
    kids_drink_price = 2

    # Define the prices of the meal deals
    burger_meal_price = 9.5
    kids_meal_price = 5

    # Calculate the total cost of buying the individual food items
    total_individual_cost = (2 * burger_price + 2 * fries_price + 2 * drink_price) + (2 * (2 * burger_price + 2 * kids_burger_price + 2 * kids_fries_price + 2 * kids_drink_price))

    # Calculate the total cost of buying the meal deals
    total_meal_cost = 2 * burger_meal_price + 2 * kids_meal_price

    # Calculate the savings
    savings = total_individual_cost - total_meal_cost

    # return the result
    result = savings
    return result

print(solution())