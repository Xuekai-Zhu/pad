def solution():
    
    sandwiches = 20
    portions = 8
    sliced_sandwiches = sandwiches * 2 * 2
    people = sliced_sandwiches // portions
    result = people
    return result

print(solution())