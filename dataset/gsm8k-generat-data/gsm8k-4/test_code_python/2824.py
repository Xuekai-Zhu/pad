def solution():
    """A taco truck buys 100 pounds of beef. They use .25 pounds of beef per taco. If they sell each taco for $2 and each taco takes $1.5 to make how much profit did they make if they used all the beef?"""
    # Define the amount of beef and the amount used per taco
    total_beef = 100
    beef_per_taco = 0.25

    # Calculate the number of tacos that can be made
    tacos_made = total_beef / beef_per_taco

    # Calculate the cost to make all the tacos
    cost_to_make = tacos_made * 1.5

    # Calculate the revenue from selling all the tacos
    revenue = tacos_made * 2

    # Calculate the profit from selling all the tacos
    profit = revenue - cost_to_make
    
    result = profit
    return result

print(solution())