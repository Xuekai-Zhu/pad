def solution():
    """The ratio of boys to girls at the dance was 3:4. There were 60 girls at the dance. The teachers were 20% of the number of boys. How many people were at the dance?"""
    girls = 60
    boys_ratio = 3/4
    boys = boys_ratio * girls
    teachers = 0.2 * boys
    total_people = girls + boys + teachers
    result = total_people
    return result

print(solution())