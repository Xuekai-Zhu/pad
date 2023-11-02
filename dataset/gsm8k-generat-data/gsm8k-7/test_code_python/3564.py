def solution():
    bread_cost = 50
    ham_cost = 150
    cake_cost = 200

    # Calculate the total cost of bread and ham
    total_cost = bread_cost + ham_cost

    # Calculate the percentage of the total cost that bread and ham make up
    percentage = ((bread_cost + ham_cost) / (bread_cost + ham_cost + cake_cost)) * 100
    result = percentage
    return result

print(solution())