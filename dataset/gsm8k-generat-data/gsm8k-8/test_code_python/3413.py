def solution():
    # Calculate the total number of seeds Mike threw to the bigger group
    bigger_group = 2 * 20

    # Calculate the total number of seeds Mike threw before the extra birds arrived
    before_extra_birds = 20 + bigger_group

    # Calculate the total number of seeds Mike threw after the extra birds arrived
    after_extra_birds = before_extra_birds + 30

    # Calculate the total number of seeds Mike started with
    total_seeds = after_extra_birds + 30
    result = total_seeds
    return result

print(solution())