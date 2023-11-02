def solution():
    """Lucca has 100 balls and 10 percent of his balls are basketballs. Lucien has 200 balls and 20 percent of them are basketballs. In total how many basketballs do Lucca and Lucien have?"""
    # Calculate the number of basketballs Lucca has
    lucca_basketballs = 0.1 * 100

    # Calculate the number of basketballs Lucien has
    lucien_basketballs = 0.2 * 200

    # Calculate the total number of basketballs
    total_basketballs = lucca_basketballs + lucien_basketballs

    # return the result
    result = total_basketballs
    return result

print(solution())