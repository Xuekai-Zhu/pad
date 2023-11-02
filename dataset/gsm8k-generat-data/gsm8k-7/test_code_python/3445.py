def solution():
    # prices for individual items
    burger_price = 5
    fries_price = 3
    drink_price = 3
    kids_burger_price = 3
    kids_fries_price = 2
    juice_price = 2

    # prices for meal deals
    burger_meal_price = 9.5
    kids_meal_price = 5

    # number of meals purchased
    num_burger_meals = 2
    num_kids_meals = 2

    # calculate total cost of meals purchased individually
    total_individual_cost = (burger_price + fries_price + drink_price) * num_burger_meals * 2  # 2 people
    total_individual_cost += (kids_burger_price + kids_fries_price + juice_price) * num_kids_meals * 4  # 4 children

    # calculate cost of meals purchased as deals
    total_deal_cost = (burger_meal_price + kids_meal_price) * 2  # 2 of each meal deal

    # calculate amount saved by buying meals as deals
    savings = total_individual_cost - total_deal_cost
    result = savings
    return result

print(solution())