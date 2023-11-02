def solution():
    """Alice likes to count the puffs of clouds in the sky while she eats her lunch outside at school. On Monday she counts just 3 puffs of clouds. Each day after that through Friday, though, she sees double the number of clouds in the sky as the day before. At the end of the week, how many clouds will she have counted in the sky at lunch across all five days?"""
    Monday_count = 3
    Tuesday_count = Monday_count * 2
    Wednesday_count = Tuesday_count * 2
    Thursday_count = Wednesday_count * 2
    Friday_count = Thursday_count * 2
    total_count = Monday_count + Tuesday_count + Wednesday_count + Thursday_count + Friday_count
    result = total_count
    return result

print(solution())