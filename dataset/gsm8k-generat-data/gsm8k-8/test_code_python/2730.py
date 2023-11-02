def solution():
    # Define the number of people planting
    num_people = 5

    # Calculate the total number of flowers planted
    total_flowers = 200

    # Calculate the number of flowers planted in one day by the group
    flowers_per_day = total_flowers / 2

    # Calculate the number of flowers planted in one day by James
    james_flowers_per_day = flowers_per_day / num_people

    result = james_flowers_per_day
    return result

print(solution())