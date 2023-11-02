def solution():
    paintings_per_day = 2
    starting_paintings = 20
    num_days = 30

    # Calculate the total number of paintings that Philip will make in 30 days
    total_paintings_made = paintings_per_day * num_days

    # Calculate the total number of paintings that Philip will have after 30 days
    total_paintings = starting_paintings + total_paintings_made
    result = total_paintings
    return result

print(solution())