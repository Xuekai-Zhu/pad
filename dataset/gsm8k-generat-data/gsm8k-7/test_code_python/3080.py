def solution():
    num_fish = 2
    num_years = 5

    # Calculate the total number of times Tony's parents buy him new fish
    num_purchases = num_years

    # Calculate the total number of fish that Tony will have after 5 years
    # Every time Tony gets two new fish, one of them dies, so the net gain is only 1 fish each time
    total_fish = num_fish + (num_purchases * 1)

    result = total_fish
    return result

print(solution())