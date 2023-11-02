def solution():
    """Iris’ family is planning a surprise birthday party for her. The party will include her 3 uncles and 4 aunts who have a son and daughter each as well as her brother and mother. In total, how many people are coming to Iris’ birthday party?"""
    # Define the number of uncles, aunts, and cousins
    num_uncles = 3
    num_aunts = 4
    num_cousins = (num_uncles + num_aunts) * 2

    # Define the number of siblings and parents
    num_siblings = 1  # Iris has one brother
    num_parents = 2  # Iris has one mother, assuming father is not mentioned

    # Calculate the total number of people coming to the party
    total_people = num_uncles + num_aunts + num_cousins + num_siblings + num_parents

    # Display the total number of people
    result = total_people
    return result

print(solution())