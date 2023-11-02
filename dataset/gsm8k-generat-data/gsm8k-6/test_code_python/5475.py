def solution():
    base_chance = 10  # starting chance of making the team
    height_increase = 10  # chance increases by 10% for every additional inch of height
    height_diff = 3  # Devin grows 3 inches
    final_height = 65 + height_diff  # Devin's final height
    final_chance = base_chance + (height_diff * height_increase)  # calculate the final chance of making the team
    result = final_chance
    return result

print(solution())