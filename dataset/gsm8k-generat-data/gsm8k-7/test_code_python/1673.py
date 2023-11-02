def solution():
    football_cost = 3.75
    shorts_cost = 2.40
    shoes_cost = 11.85
    available_money = 10

    # Calculate the total cost of all items
    total_cost = football_cost + shorts_cost + shoes_cost

    # Calculate how much more money Zachary needs
    needed_money = total_cost - available_money
    result = needed_money
    return result

print(solution())