def solution():
    starting_seashells = 180  # Ali started with 180 seashells
    given_away_seashells = 40 + 30  # Ali gave away a total of 70 seashells
    remaining_seashells = starting_seashells - given_away_seashells  # Ali has this many seashells left
    sold_seashells = remaining_seashells / 2  # Ali sold half of the remaining seashells
    remaining_seashells -= sold_seashells  # Update the remaining seashells

    result = remaining_seashells
    return result

print(solution())