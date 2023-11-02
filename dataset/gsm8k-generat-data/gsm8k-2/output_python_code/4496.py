def solution():
    """Paddy's Confidential has 600 cans of stew required to feed 40 people. How many cans would be needed to feed 30% fewer people?"""
    initial_people = 40
    initial_cans = 600
    reduced_people = int(initial_people * 0.7)  # 30% fewer people
    reduced_cans = (initial_cans * reduced_people) / initial_people
    result = reduced_cans
    return result

print(solution())