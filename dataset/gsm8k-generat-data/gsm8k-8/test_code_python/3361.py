def solution():
    # Define Agnes' current age and Jane's current age
    agnes_age = 25
    jane_age = 6

    # Let x be the number of years until Agnes is twice as old as Jane
    x = 0

    # Increment x until Agnes is twice as old as Jane
    while agnes_age != 2 * jane_age:
        x += 1
        agnes_age += 1
        jane_age += 1

    result = x
    return result

print(solution())