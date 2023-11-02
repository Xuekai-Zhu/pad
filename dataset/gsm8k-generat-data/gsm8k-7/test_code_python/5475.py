def solution():
    initial_chance = 0.1  # 10% chance for 66 inches
    height = 65  # initial height
    additional_inches = 3  # height increase
    increase_per_inch = 0.1  # 10% increase per inch of height

    # Calculate final height
    final_height = height + additional_inches

    # Calculate total increase in chance of making the team
    total_increase = additional_inches * increase_per_inch

    # Calculate final chance of making the team
    final_chance = initial_chance + total_increase

    result = final_chance
    return result

print(solution())