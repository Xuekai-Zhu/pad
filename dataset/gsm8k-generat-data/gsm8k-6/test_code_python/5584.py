def solution():
    # Calculate the number of people voting for Biff and undecided
    biff_percentage = 45
    undecided_percentage = 8
    biff_and_undecided = biff_percentage + undecided_percentage

    # Calculate the number of people voting for Marty
    marty_percentage = 100 - biff_and_undecided
    marty_voters = (marty_percentage / 100) * 200
    result = marty_voters
    return result

print(solution())