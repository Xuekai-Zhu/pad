def solution():
    """Donna is catering for a party. She makes 20 sandwiches and then cuts them in half, before cutting them in half again. She then gives everyone 8 portions. How many people can she feed?"""
    sandwiches = 20
    portions = 8
    sliced_sandwiches = sandwiches * 2 * 2
    people = sliced_sandwiches // portions
    result = people
    return result

print(solution())