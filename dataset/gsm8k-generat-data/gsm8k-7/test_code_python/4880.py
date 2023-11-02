def solution():
    num_cheeseburgers = 2
    cheeseburger_price = 3

    num_milkshakes = 2
    milkshake_price = 5

    num_cheese_fries = 1
    cheese_fries_price = 8

    percent_spent = 0.8
    jim_money = 20

    # Calculate the total cost of their order
    total_order_cost = (num_cheeseburgers * cheeseburger_price) + (num_milkshakes * milkshake_price) + (num_cheese_fries * cheese_fries_price)

    # Calculate the total amount of money they spent (80% of combined money)
    total_spent = percent_spent * (jim_money + cousin_money)

    # Calculate how much Jim's cousin brought
    cousin_money = total_spent - jim_money
    result = cousin_money
    return result

print(solution())