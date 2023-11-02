def solution():
    # Calculate Sam's daily animal count
    sam_animals = 6

    # Calculate Rob's daily animal count
    rob_animals = sam_animals / 2

    # Calculate the total animal count of Rob and Sam
    total_animals = sam_animals + rob_animals

    # Calculate Mark's daily animal count
    mark_animals = (1/3) * total_animals

    # Calculate Peter's daily animal count
    peter_animals = 3 * mark_animals

    # Calculate the total daily animal count
    total_daily_animals = sam_animals + rob_animals + mark_animals + peter_animals
    result = total_daily_animals
    return result

print(solution())