def solution():
    # Individual prices
    burger_price = 5
    fries_price = 3
    drink_price = 3
    kids_burger_price = 3
    kids_fries_price = 2
    kids_drink_price = 2

    # Prices for meal deals
    burger_meal_price = 9.5
    kids_meal_price = 5

    # Calculate individual prices for 6 meals
    total_price_individual = (2*burger_price + 2*fries_price + 2*drink_price) + (2*burger_price + 2*kids_burger_price + 2*kids_fries_price + 2*kids_drink_price)

    # Calculate prices for 6 meal deals
    total_price_meal_deal = (2*burger_meal_price) + (2*kids_meal_price)

    # Calculate the savings
    savings = total_price_individual - total_price_meal_deal
    result = savings
    return result

print(solution())