def solution():
    """Roberta takes $158 with her on a shopping trip to the mall. She spends $45 on new shoes, $17 less on a new bag, and a quarter of the price of the bag for lunch. How much money does she have left after these purchases?"""
    # Define the initial amount of money Roberta had
    initial_money = 158

    # Calculate the cost of the shoes
    shoe_cost = 45

    # Calculate the cost of the bag
    bag_cost = shoe_cost - 17

    # Calculate the cost of lunch
    lunch_cost = bag_cost / 4

    # Calculate the total cost of all purchases
    total_cost = shoe_cost + bag_cost + lunch_cost

    # Calculate the amount of money Roberta has left after the purchases
    money_left = initial_money - total_cost

    # Display the amount of money Roberta has left
    result = money_left
    return result

print(solution())