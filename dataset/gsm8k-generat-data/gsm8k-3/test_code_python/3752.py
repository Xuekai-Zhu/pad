def solution():
    """Lucca has 100 balls and 10 percent of his balls are basketballs. Lucien has 200 balls and 20 percent of them are basketballs. In total how many basketballs do Lucca and Lucien have?"""

    # Number of basketballs Lucca has
    lucca_basketballs = 0.1 * 100

    # Number of basketballs Lucien has
    lucien_basketballs = 0.2 * 200

    # Total number of basketballs
    total_basketballs = lucca_basketballs + lucien_basketballs

    # Display the total number of basketballs
    result = total_basketballs
    return result

print(solution())