def solution():
    """Donna is catering for a party. She makes 20 sandwiches and then cuts them in half, before cutting them in half again. She then gives everyone 8 portions. How many people can she feed?"""
    num_sandwiches = 20
    portions_per_sandwich = 4
    total_portions = num_sandwiches * portions_per_sandwich
    num_people = total_portions // 8
    result = num_people
    return result

print(solution())