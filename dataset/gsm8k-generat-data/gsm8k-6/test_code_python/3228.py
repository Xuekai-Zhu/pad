def solution():
    # Calculate the total cost of breakfast and lunch
    total_breakfast = 2 + 4  # muffin costs $2 and coffee costs $4
    total_lunch = 3 + 5.25 + 0.75  # soup costs $3, salad costs $5.25, and lemonade costs $0.75

    # Calculate the difference in cost between lunch and breakfast
    cost_difference = total_lunch - total_breakfast
    result = cost_difference
    return result

print(solution())