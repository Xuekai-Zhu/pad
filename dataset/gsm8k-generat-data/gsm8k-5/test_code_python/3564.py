def solution():
    # Calculate the total cost of ham and bread
    ham_cost = 150
    bread_cost = 50
    total_cost = ham_cost + bread_cost

    # Calculate the percentage of the cost that is ham and bread
    percentage = (total_cost / (ham_cost + bread_cost + 200)) * 100

    result = percentage
    return result

print(solution())