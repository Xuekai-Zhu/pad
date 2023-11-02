def solution():
    """A survey conducted by the school showed that only 20% of the 800 parents agree to a tuition fee increase. How many parents disagree with the tuition fee increase?"""
    # Define the total number of parents and the percentage that agrees to a tuition fee increase
    total_parents = 800
    agree_percentage = 20

    # Calculate the number of parents who agree to a tuition fee increase
    agree_parents = (agree_percentage / 100) * total_parents

    # Calculate the number of parents who disagree with a tuition fee increase
    disagree_parents = total_parents - agree_parents

    result = disagree_parents
    return result

print(solution())