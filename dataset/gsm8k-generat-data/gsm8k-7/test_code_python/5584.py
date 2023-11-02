def solution():
    num_people_polled = 200
    biff_percent = 45
    undecided_percent = 8

    # Calculate the percentage of people who said they are voting for Marty
    marty_percent = 100 - biff_percent - undecided_percent

    # Calculate the number of people who said they are voting for Marty
    num_marty_voters = (marty_percent/100) * num_people_polled
    result = num_marty_voters
    return result

print(solution())