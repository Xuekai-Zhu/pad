def solution():
    num_people = 5  # James and 4 friends
    total_flowers = 200
    num_days = 2

    # Calculate the total number of flowers planted by each person
    flowers_per_person = total_flowers / num_people

    # Calculate the number of flowers planted by James in one day
    james_flowers_per_day = flowers_per_person / num_days
    result = james_flowers_per_day
    return result

print(solution())