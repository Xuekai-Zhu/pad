def solution():
    """James and 4 of his friends volunteered to plant flowers. In 2 days, they were able to plant a total of 200 flowers. If each of them planted the same number of flowers, how many flowers did James plant in a day?"""
    # Total number of people planting flowers
    total_people = 5

    # Total number of days
    total_days = 2

    # Total number of flowers planted
    total_flowers = 200

    # Calculate the number of flowers planted per person per day
    flowers_per_person_per_day = total_flowers / (total_people * total_days)

    # Calculate the number of flowers James planted in a day
    james_flowers_per_day = flowers_per_person_per_day

    # Display the number of flowers James planted in a day
    result = james_flowers_per_day
    return result

print(solution())