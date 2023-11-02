def solution():
    """John arm wrestles 20 people. He beats 80%. How many people did he lose to?"""
    total_people = 20
    winning_percent = 80
    losing_percent = 100 - winning_percent
    people_lost_to = total_people * (losing_percent / 100)
    result = people_lost_to
    return result

print(solution())