def solution():
    tyler_money = 100
    num_scissors = 8
    scissors_price = 5
    num_erasers = 10
    erasers_price = 4

    # Calculate the total cost of all scissors
    total_scissors_cost = num_scissors * scissors_price

    # Calculate the total cost of all erasers
    total_erasers_cost = num_erasers * erasers_price

    # Calculate the total cost of all items
    total_cost = total_scissors_cost + total_erasers_cost

    # Calculate how much of Tyler's money remains
    remaining_money = tyler_money - total_cost
    result = remaining_money
    return result

print(solution())