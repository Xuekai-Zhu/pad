def solution():
    """Chandra is going on a monster hunt. After a big storm, there have been lost monsters all around the castle grounds for the last 5 days. Chandra wants to rope them all up and return them to the swamps where they will be the most comfortable. On the first day she saw 2 monsters near the castle walls. Every day after that she saw double the amount as the day before. After 5 days how many monsters does she need to lead back to the swamps?"""
    first_day_monsters = 2
    total_monsters = 0
    for i in range(5):
        daily_monsters = first_day_monsters * (2 ** i)
        total_monsters += daily_monsters
    result = total_monsters
    return result

print(solution())