def solution():
    """Roberta takes $158 with her on a shopping trip to the mall. She spends $45 on new shoes, $17 less on a new bag, and a quarter of the price of the bag for lunch. How much money does she have left after these purchases?"""
    # Define the initial amount of money Roberta has
    initial_money = 158

    # Define the cost of the shoes and bag
    shoes_cost = 45
    bag_cost = shoes_cost - 17

    # Define the cost of lunch
    lunch_cost = bag_cost / 4

    # Calculate the total amount spent
    total_spent = shoes_cost + bag_cost + lunch_cost

    # Calculate the total amount of money left
    money_left = initial_money - total_spent

    result = money_left
    return result

print(solution())