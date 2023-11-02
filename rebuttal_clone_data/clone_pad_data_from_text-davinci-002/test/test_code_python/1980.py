def solution():
    sandwiches = 20
    sandwich_halves = sandwiches * 2
    sandwich_quarters = sandwich_halves * 2
    portions = 8
    people = sandwich_quarters / portions
    result = people
    
    return result

print(solution())