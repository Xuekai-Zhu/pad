def solution():
    """Chandra is going on a monster hunt. After a big storm, there have been lost monsters all around the castle grounds for the last 5 days. Chandra wants to rope them all up and return them to the swamps where they will be the most comfortable. On the first day she saw 2 monsters near the castle walls. Every day after that she saw double the amount as the day before. After 5 days how many monsters does she need to lead back to the swamps?"""
    # Define the number of monsters on the first day
    day1_monsters = 2

    # Calculate the number of monsters on each day
    day2_monsters = day1_monsters * 2
    day3_monsters = day2_monsters * 2
    day4_monsters = day3_monsters * 2
    day5_monsters = day4_monsters * 2

    # Calculate the total number of monsters seen over the 5 days
    total_monsters = day1_monsters + day2_monsters + day3_monsters + day4_monsters + day5_monsters

    # Display the total number of monsters
    result = total_monsters
    return result

print(solution())