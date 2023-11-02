def solution():
    """A taco truck buys 100 pounds of beef.  They use .25 pounds of beef per taco.  If they sell each taco for $2 and each taco takes $1.5 to make how much profit did they make if they used all the beef?"""
    # Define the amount of beef per taco
    BEEF_PER_TACO = 0.25

    # Calculate the number of tacos that can be made from 100 pounds of beef
    tacos = 100 / BEEF_PER_TACO

    # Calculate the total revenue from selling all the tacos
    total_revenue = tacos * 2

    # Calculate the total cost of making all the tacos
    total_cost = tacos * 1.5

    # Calculate the profit made from selling all the tacos
    profit = total_revenue - total_cost

    # Display the profit
    result = profit
    return result

print(solution())