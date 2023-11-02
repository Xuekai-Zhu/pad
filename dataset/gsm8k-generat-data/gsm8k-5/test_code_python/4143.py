def solution():
    # Calculate the initial number of people in the cars
    initial_people = 20 * 3  # 20 cars, each with 2 passengers and 1 driver

    # Calculate the additional number of people in the cars after passing the halfway point
    additional_people = 20  # Each car gains one additional passenger

    # Calculate the total number of people in the cars by the end of the race
    total_people = initial_people + additional_people
    result = total_people
    return result

print(solution())