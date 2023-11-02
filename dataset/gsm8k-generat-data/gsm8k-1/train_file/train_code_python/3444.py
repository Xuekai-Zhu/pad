def solution():
    """
    At the burger hut, you can buy a burger for $5, french fries for $3, and a soft drink for $3.
    If you order a special burger meal, you get all 3 of these food items for $9.50.
    A kid’s burger is $3, a kid’s french fries are $2, and a kid's juice box is $2.
    They also have a kids meal of all 3 kids' food items for $5.
    Mr. Parker buys 2 burger meals for his wife and himself.
    He also buys 2 burger meals and 2 kid's meals for his 4 children.
    How much money does Mr. Parker save by buying the 6 meals versus buying the individual food items?
    """
    burger_meal_price = 9.5
    individual_burger_price = 5
    individual_fries_price = 3
    individual_drink_price = 3
    kids_meal_price = 5
    individual_kids_burger_price = 3
    individual_kids_fries_price = 2
    individual_juice_price = 2
    
    # cost of 2 burger meals for Mr. Parker and his wife
    cost_of_2_burger_meals = burger_meal_price * 2
    
    # cost of 2 burger meals and 2 kids meals for Mr. Parker's 4 children
    cost_of_2_burger_meals_and_2_kids_meals = (burger_meal_price * 2) + (kids_meal_price * 2)
    
    # cost of individual food items for the same meals
    cost_of_individual_items = (2 * individual_burger_price) + (2 * individual_fries_price) + (2 * individual_drink_price) + (2 * kids_meal_price) + (4 * individual_kids_burger_price) + (4 * individual_kids_fries_price) + (4 * individual_juice_price)
    
    # calculate the total savings
    total_savings = cost_of_individual_items - (cost_of_2_burger_meals + cost_of_2_burger_meals_and_2_kids_meals)
    
    return total_savings

print(solution())