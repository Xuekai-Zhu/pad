def solution():
    """A normal lemon tree produces 60 lemons per year. Jim has specially engineered lemon trees that produce 50% more lemons per year. He has a grove that is 50 trees by 30 trees. How many lemons does he produce in 5 years?"""
    # Define the number of trees in the grove
    num_trees = 50 * 30

    # Calculate the number of lemons produced per tree per year
    lemons_per_tree = 60 * 1.5

    # Calculate the total number of lemons produced per year
    total_lemons_per_year = num_trees * lemons_per_tree

    # Calculate the total number of lemons produced in 5 years
    total_lemons = total_lemons_per_year * 5

    result = total_lemons
    return result

print(solution())