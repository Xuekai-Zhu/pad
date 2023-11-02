def solution():
    initial_chance = 0.1 # 10%
    starting_height = 66
    additional_chance_per_inch = 0.1 # 10%

    # Calculate the chance of making the team with starting height
    current_chance = initial_chance

    # Calculate the chance of making the team with added height
    added_height = 3
    added_chance = added_height * additional_chance_per_inch

    # Add the chances together
    total_chance = current_chance + added_chance
    result = total_chance
    return result

print(solution())