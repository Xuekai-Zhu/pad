def solution():
    """James and 4 of his friends volunteered to plant flowers. In 2 days, they were able to plant a total of 200 flowers. If each of them planted the same number of flowers, how many flowers did James plant in a day?"""
    # Define the total number of volunteers
    total_volunteers = 5

    # Define the total number of days worked
    total_days = 2

    # Calculate the total number of flowers planted
    total_flowers = 200

    # Calculate the average number of flowers planted per person per day
    flowers_per_person_per_day = total_flowers / (total_volunteers * total_days)

    # Calculate the number of flowers James planted in a day
    james_flowers_per_day = flowers_per_person_per_day

    # Return the result
    result = james_flowers_per_day
    return result

print(solution())