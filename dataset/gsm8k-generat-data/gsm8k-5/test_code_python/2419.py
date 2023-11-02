def solution():
    total_meat_needed = 210  # The bear needs 210 pounds of meat in a week
    cubs_meat_needed = 35 * 4  # The bear's four cubs need 35 pounds each per week
    bear_meat_needed = total_meat_needed - cubs_meat_needed  # The bear needs to catch the remaining amount of meat
    rabbits_needed = bear_meat_needed / 5  # Each rabbit provides 5 pounds of meat
    rabbits_per_day = rabbits_needed / 7  # The bear hunts daily, so divide by 7 days in a week

    result = rabbits_per_day
    return result

print(solution())