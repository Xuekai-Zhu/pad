def solution():
    """In a court-mandated traffic class, there are a certain number of drunk drivers and 3 less than 7 times that many speeders. If there are 45 students total, how many drunk drivers are there?"""
    # Let x be the number of drunk drivers, then the number of speeders is 7x - 3
    # The total number of students is x + (7x - 3) = 8x - 3
    # Set the total number of students to 45 and solve for x
    x = (45 + 3) / 8
    # Round down to the nearest integer to get the number of drunk drivers
    num_drunk_drivers = int(x)
    result = num_drunk_drivers
    return result

print(solution())