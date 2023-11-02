def solution():
    """Bob bought 2 show dogs for $250.00 each to breed as a side business.  The female just had a litter of 6 puppies.  If he sells each puppy for $350.00, what is his total profit?"""
    # Define the cost of each show dog
    DOG_COST = 250

    # Calculate the total cost of the show dogs
    total_dog_cost = DOG_COST * 2

    # Calculate the total revenue from selling the puppies
    puppy_revenue = 6 * 350

    # Calculate the total profit
    total_profit = puppy_revenue - total_dog_cost

    # Display the total profit
    result = total_profit
    return result

print(solution())