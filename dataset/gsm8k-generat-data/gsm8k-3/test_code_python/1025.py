def solution():
    """A survey conducted by the school showed that only 20% of the 800 parents agree to a tuition fee increase. How many parents disagree with the tuition fee increase?"""
    # Define the total number of parents surveyed
    total_parents = 800

    # Calculate the number of parents who agreed to the tuition fee increase
    agree_parents = total_parents * 0.2

    # Calculate the number of parents who disagreed with the tuition fee increase
    disagree_parents = total_parents - agree_parents

    # Display the number of parents who disagreed with the tuition fee increase
    result = disagree_parents
    return result

print(solution())