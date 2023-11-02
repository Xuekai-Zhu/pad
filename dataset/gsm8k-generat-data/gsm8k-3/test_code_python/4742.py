def solution():
    """It costs Molly $5 per package to send Christmas gifts to her relatives by mail.  She has two parents and three brothers, and each of her brothers is married with 2 children each.  If she sends one package to each relative by mail, how much does it cost her to send all of the gifts by mail to her relatives, in dollars?"""
    # Define the number of packages to be sent
    num_packages = 2 + 3 + (3*2) + 1 # 2 parents, 3 brothers, 3 brothers' spouses, 6 brothers' children, and herself
    
    # Calculate the total cost of sending all the packages
    total_cost = num_packages * 5

    # Display the total cost
    result = total_cost
    return result

print(solution())