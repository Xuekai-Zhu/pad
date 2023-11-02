def solution():
    # Calculate the cost of the bag
    bag_cost = 45 - 17  # Roberta spends $17 less on a new bag than on new shoes

    # Calculate the cost of lunch
    lunch_cost = bag_cost / 4  # Roberta spends a quarter of the price of the bag on lunch

    # Calculate the total cost of her purchases
    total_cost = shoes_cost + bag_cost + lunch_cost

    # Calculate the amount of money she has left
    money_left = 158 - total_cost
    result = money_left
    return result

print(solution())