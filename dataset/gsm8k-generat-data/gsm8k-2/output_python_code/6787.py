def solution():
    """Roberta takes $158 with her on a shopping trip to the mall. She spends $45 on new shoes, $17 less on a new bag, and a quarter of the price of the bag for lunch. How much money does she have left after these purchases?"""
    shopping_money = 158
    shoes_cost = 45
    bag_cost = shoes_cost - 17
    lunch_cost = bag_cost / 4
    total_spent = shoes_cost + bag_cost + lunch_cost
    remaining_money = shopping_money - total_spent
    result = remaining_money
    return result

print(solution())