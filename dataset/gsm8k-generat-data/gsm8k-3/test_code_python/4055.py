def solution():
    """Every year, four clowns and thirty children go on a carousel. This year, the candy seller, at the carousel, had 700 candies. The candy seller then sold 20 candies, to each of the clowns and the children, who attended. How many candies did he have left?"""
    # Define the number of clowns and children
    num_clowns = 4
    num_children = 30

    # Define the initial number of candies
    num_candies = 700

    # Calculate the total number of candies sold
    total_candies_sold = (num_clowns + num_children) * 20

    # Calculate the number of candies left
    candies_left = num_candies - total_candies_sold

    # Display the number of candies left
    result = candies_left
    return result

print(solution())