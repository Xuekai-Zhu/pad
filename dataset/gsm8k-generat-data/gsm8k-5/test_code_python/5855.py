def solution():
    remaining_gummy_worms = 4  # Carlos has 4 gummy worms left
    days_of_eating = 4  # Carlos has been eating for 4 days
    for i in range(days_of_eating):
        remaining_gummy_worms *= 2  # Carlos ate half of the remaining gummy worms each day
    initial_gummy_worms = remaining_gummy_worms * 2  # Carlos had the remaining gummy worms plus the ones he ate on the fourth day
    result = initial_gummy_worms
    return result

print(solution())