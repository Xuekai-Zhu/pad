def solution():
    """John decides to buy a month's supply of dog treats.  He gives his dog 2 treats a day and they cost $.1 each.  How much does he spend on the treats if the month is 30 days long?"""
    # Define the number of treats per day and the cost per treat
    treats_per_day = 2
    cost_per_treat = 0.1

    # Calculate the total number of treats for the month
    treats_per_month = treats_per_day * 30

    # Calculate the total cost of the treats for the month
    total_cost = treats_per_month * cost_per_treat

    # Display the total cost
    result = total_cost
    return result

print(solution())