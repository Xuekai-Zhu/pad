def solution():
    """A single train car can carry 60 passengers. A 747 airplane can carry 366 passengers. How many more passengers can a train with 16 cars carry than 2 airplanes?"""
    # Define the capacity of a train car and an airplane
    TRAIN_CAPACITY = 60
    AIRPLANE_CAPACITY = 366

    # Calculate the total capacity of 16 train cars and 2 airplanes
    train_capacity = TRAIN_CAPACITY * 16
    airplane_capacity = AIRPLANE_CAPACITY * 2

    # Calculate the difference in capacity between the train and airplanes
    capacity_difference = train_capacity - airplane_capacity

    # Display the difference in capacity
    result = capacity_difference
    return result

print(solution())