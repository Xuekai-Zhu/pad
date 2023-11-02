def solution():
    # Calculate the number of Toyota trucks
    num_toyota = 5 * 2  # there are twice as many Ford trucks as Toyota trucks, and there are 5 Volkswagen Bugs

    # Calculate the number of Ford trucks
    num_ford = num_toyota * 2  # there are twice as many Ford trucks as Toyota trucks

    # Calculate the number of Dodge trucks
    num_dodge = num_ford * 3  # there are one-third as many Ford trucks as Dodge trucks

    result = num_dodge
    return result

print(solution())