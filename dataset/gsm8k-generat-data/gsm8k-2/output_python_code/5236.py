def solution():
    """Wanda walks her daughter .5 miles to school in the morning and then walks .5 miles home. She repeats this when she meets her daughter after school in the afternoon. They walk to school 5 days a week. How many miles does Wanda walk after 4 weeks?"""
    morning_walk = 0.5
    afternoon_walk = 0.5
    days_per_week = 5
    weeks = 4
    total_distance = (morning_walk + afternoon_walk) * days_per_week * weeks
    result = total_distance
    return result

print(solution())