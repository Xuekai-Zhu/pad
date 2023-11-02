def solution():
    # Calculate the number of tacos that can be made with 100 pounds of beef
    tacos = 100 // 0.25

    # Calculate the total revenue from selling all the tacos
    revenue = tacos * 2

    # Calculate the total cost of making all the tacos
    cost = tacos * 1.5

    # Calculate the profit
    profit = revenue - cost
    result = profit
    return result

print(solution())