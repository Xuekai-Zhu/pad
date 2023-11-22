def solution():
    
    # Define the initial cost to plant the tree and the cost to feed the tree
    tree_cost = 90
    feed_cost = 3

    # Calculate the total cost to feed the tree and grow 7 lemons each year
    total_cost = feed_cost * 7

    # Calculate the number of years it will take to earn enough money
    years = tree_cost / total_cost

    # Display the number of years
    result = years
    return result

print(solution())