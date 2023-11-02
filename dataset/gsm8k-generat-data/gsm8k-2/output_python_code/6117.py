def solution():
    """A single train car can carry 60 passengers. A 747 airplane can carry 366 passengers. How many more passengers can a train with 16 cars carry than 2 airplanes?"""
    train_capacity = 60 * 16
    airplane_capacity = 366 * 2
    extra_passengers = train_capacity - airplane_capacity
    result = extra_passengers
    return result

print(solution())