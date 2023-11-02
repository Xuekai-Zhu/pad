def solution():
    beef_in_pounds = 100  # The taco truck buys 100 pounds of beef
    beef_per_taco = 0.25  # The taco truck uses 0.25 pounds of beef per taco

    tacos_sold = beef_in_pounds / beef_per_taco  # Calculate the number of tacos sold
    revenue = tacos_sold * 2  # Calculate the total revenue from selling tacos
    cost = tacos_sold * 1.5  # Calculate the total cost of making the tacos
    profit = revenue - cost  # Calculate the profit from selling tacos

    result = profit
    return result

print(solution())