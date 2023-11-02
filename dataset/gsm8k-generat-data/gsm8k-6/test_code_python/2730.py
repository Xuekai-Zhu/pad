def solution():
    # Calculate the total number of flowers planted by James and his friends
    total_flowers_planted = 200

    # Calculate the number of flowers planted by each person
    num_people = 5  # James and his 4 friends
    flowers_per_person = total_flowers_planted / num_people

    # Calculate the number of flowers planted by James in one day (assuming they worked equally hard each day)
    flowers_per_day_James = flowers_per_person / 2

    result = flowers_per_day_James
    return result

print(solution())