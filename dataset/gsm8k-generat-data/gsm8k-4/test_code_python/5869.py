def solution():
    """Jaden had 14 toy cars. Then he bought 28 cars from the toy store and got 12 cars for his birthday. Jaden gave 8 of the toy cars to his sister and 3 to his friend Vinnie. How many toy cars does Jaden have left?"""
    # Initialize the number of toy cars Jaden had
    toy_cars = 14

    # Add the number of toy cars Jaden bought from the store
    toy_cars += 28

    # Add the number of toy cars Jaden got for his birthday
    toy_cars += 12

    # Subtract the number of toy cars Jaden gave to his sister and friend
    toy_cars -= 8
    toy_cars -= 3

    # return the result
    result = toy_cars
    return result

print(solution())