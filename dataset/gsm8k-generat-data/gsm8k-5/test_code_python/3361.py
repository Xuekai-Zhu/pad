def solution():
    agnes_age = 25
    jane_age = 6

    # Initialize the number of years
    years = 0

    # Keep incrementing the years until Agnes is twice as old as Jane
    while agnes_age != 2 * jane_age:
        years += 1
        agnes_age += 1
        jane_age += 1

    result = years
    return result

print(solution())