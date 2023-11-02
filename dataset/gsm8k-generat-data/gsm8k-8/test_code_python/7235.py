def solution():
    # Define Jenny's age in terms of Charlie's age
    jenny_age = 5 + charlie_age

    # Define Bobby's age in terms of Charlie's age
    bobby_age = charlie_age - 3

    # Set up a loop to find when Jenny will be twice as old as Bobby
    while jenny_age != 2 * bobby_age:
        jenny_age += 1
        bobby_age += 1

    # When the loop finishes, Charlie's age will be one less than Jenny's age
    charlie_age = jenny_age - 1

    # Return Charlie's age
    result = charlie_age
    return result

print(solution())