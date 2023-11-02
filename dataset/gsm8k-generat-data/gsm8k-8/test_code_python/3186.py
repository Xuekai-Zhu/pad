def solution():
    # Define the number of monsters seen on the first day
    day1_monsters = 2

    # Calculate the number of monsters seen each day after that
    day2_monsters = day1_monsters * 2
    day3_monsters = day2_monsters * 2
    day4_monsters = day3_monsters * 2
    day5_monsters = day4_monsters * 2

    # Calculate the total number of monsters seen over the 5 days
    total_monsters = day1_monsters + day2_monsters + day3_monsters + day4_monsters + day5_monsters
    result = total_monsters
    return result

print(solution())