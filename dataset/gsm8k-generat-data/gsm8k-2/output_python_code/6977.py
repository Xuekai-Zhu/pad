def solution():
    """There are 4 wolves out hunting for the pack. The pack contains 16 additional wolves. Each wolf needs to eat 8 pounds of meat a day and the wolves won't hunt again for five days. If each deer contains 200 pounds of meat, how many deer does each wolf need to kill?"""
    total_wolves = 20
    daily_meat_needed = 8 * total_wolves
    meat_needed_for_5_days = daily_meat_needed * 5
    meat_per_deer = 200
    deer_needed = meat_needed_for_5_days / meat_per_deer
    deer_per_wolf = deer_needed / total_wolves
    result = deer_per_wolf
    return result

print(solution())