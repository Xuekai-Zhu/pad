def solution():
    # Calculate the total number of passengers a train with 16 cars can carry
    train_capacity = 60 * 16

    # Calculate the total number of passengers 2 airplanes can carry
    airplane_capacity = 366 * 2

    # Calculate the difference in the number of passengers each can carry
    difference = train_capacity - airplane_capacity
    result = difference
    return result

print(solution())