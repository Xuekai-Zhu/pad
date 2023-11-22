def solution():
    
    # Define the initial amount of money Joe has
    initial_money = 50

    # Calculate the discounted price of the shirt
    shirt_price = 25

    # Calculate the discounted price of the pair of shorts
    shorts_price = 35

    # Calculate the discounted price of the outfit
    discounted_price = shirt_price * 0.7

    # Calculate the total cost of the outfit
    total_cost = discounted_price + shorts_price

    # Calculate the amount of money Joe will have left after the purchase
    money_left = initial_money - total_cost

    # Display the amount of money Joe will have left
    result = money_left
    return result

print(solution())