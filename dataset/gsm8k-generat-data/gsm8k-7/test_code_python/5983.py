def solution():
    starting_people = 0  # starting number of people at the beach
    new_people = 100  # number of people who joined during the day
    leaving_people = 40  # number of people who left at 5:00

    # Calculate the total number of people at the beach
    total_people = starting_people + new_people - leaving_people
    result = total_people
    return result

print(solution())