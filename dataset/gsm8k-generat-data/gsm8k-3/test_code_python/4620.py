def solution():
    """It takes 5 people to lift a car and twice as many people to lift a truck. How many people are needed to lift 6 cars and 3 trucks?"""
    # Define the number of people required to lift a car and a truck
    CAR_PEOPLE = 5
    TRUCK_PEOPLE = 2 * CAR_PEOPLE

    # Define the number of cars and trucks to be lifted
    num_cars = 6
    num_trucks = 3

    # Calculate the total number of people required
    total_people = (num_cars * CAR_PEOPLE) + (num_trucks * TRUCK_PEOPLE)

    # Display the total number of people required
    result = total_people
    return result

print(solution())