def solution():
    """DJ Snake's friends decided to give him treats to celebrate his engagement. Moksi took him and his fiancee to a luxurious hotel for two nights at $4000 per night. Lil Jon bought them a car worth $30000, and Wynter presented them with a house worth four times the value of the car Lil Jon bought them. What was the total value of all the treats DJ Snake received on his engagement day?"""
    # Calculate the cost of the hotel stay
    hotel_cost = 4000 * 2

    # Calculate the cost of the car
    car_cost = 30000

    # Calculate the value of the house
    house_value = 4 * car_cost

    # Calculate the total value of all the treats
    total_value = hotel_cost + car_cost + house_value

    # Display the total value
    result = total_value
    return result

print(solution())