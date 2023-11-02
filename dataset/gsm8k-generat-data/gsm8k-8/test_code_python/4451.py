def solution():
    # Calculate how many m&m's Cheryl ate in total
    total_eaten = 7 + 5

    # Calculate how many m&m's Cheryl has left
    remaining = 25 - total_eaten

    # Calculate how many m&m's Cheryl gave to her sister
    sister_share = total_eaten - remaining

    result = sister_share
    return result

print(solution())