def solution():
    # Initialize the number of passengers to 0
    num_passengers = 0

    # Add 7 passengers at the first stop
    num_passengers += 7

    # Subtract 3 passengers and add 5 passengers at the second stop
    num_passengers -= 3
    num_passengers += 5

    # Subtract 2 passengers and add 4 passengers at the third stop
    num_passengers -= 2
    num_passengers += 4

    result = num_passengers
    return result

print(solution())