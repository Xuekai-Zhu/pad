def solution():
    """A bus has a carrying capacity of 80 people. At the first pickup point, the number of people who entered the bus was 3/5 of its carrying capacity. If there were 50 people at the next pick-up point, how many people could not take the bus because it was full?"""
    # Define the carrying capacity of the bus
    carrying_capacity = 80

    # Calculate the number of people who entered the bus at the first pickup point
    first_pickup = carrying_capacity * (3/5)

    # Calculate the number of people who entered the bus at the second pickup point
    second_pickup = 50

    # Calculate the total number of people on the bus
    total_people = first_pickup + second_pickup

    # Calculate the number of people who could not take the bus
    no_space = total_people - carrying_capacity

    # return the result
    result = no_space
    return result

print(solution())