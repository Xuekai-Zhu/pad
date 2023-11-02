def solution():
    # Calculate the number of tacos that can be made with 100 pounds of beef
    tacos_made = 100 / 0.25  # using 0.25 pounds of beef per taco

    # Calculate the total revenue from selling all the tacos
    revenue = tacos_made * 2  # selling each taco for $2

    # Calculate the total cost of making all the tacos
    cost = tacos_made * 1.5  # each taco takes $1.5 to make

    # Calculate the total profit
    profit = revenue - cost

    result = profit
    return result

print(solution())