def solution():
    """Chandra is going on a monster hunt. After a big storm, there have been lost monsters all around the castle grounds for the last 5 days. Chandra wants to rope them all up and return them to the swamps where they will be the most comfortable. On the first day she saw 2 monsters near the castle walls. Every day after that she saw double the amount as the day before. After 5 days how many monsters does she need to lead back to the swamps?"""
    # Initialize the number of monsters on the first day
    monsters = 2

    # Double the number of monsters seen each day for 5 days
    for i in range(5):
        monsters *= 2

    # Return the total number of monsters seen in 5 days
    result = monsters
    return result

print(solution())