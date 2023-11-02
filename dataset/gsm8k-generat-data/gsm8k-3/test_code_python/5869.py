def solution():
    """Jaden had 14 toy cars. Then he bought 28 cars from the toy store and got 12 cars for his birthday. Jaden gave 8 of the toy cars to his sister and 3 to his friend Vinnie. How many toy cars does Jaden have left?"""
    # Define the initial number of toy cars
    initial_cars = 14

    # Calculate the total number of toy cars Jaden has after buying and receiving more
    total_cars = initial_cars + 28 + 12

    # Subtract the number of toy cars Jaden gave away
    total_cars -= 8 + 3

    # Display the number of toy cars Jaden has left
    result = total_cars
    return result

print(solution())