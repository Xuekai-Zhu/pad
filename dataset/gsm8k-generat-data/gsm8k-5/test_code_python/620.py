def solution():
    initial_rabbits = 13
    additional_rabbits = 7
    total_rabbits = initial_rabbits + additional_rabbits

    # Let x be the number of rabbits Jasper saw in the park today
    # We know that 3 * total_rabbits = x
    # Solving for x:
    jasper_saw = 3 * total_rabbits
    result = jasper_saw
    return result

print(solution())