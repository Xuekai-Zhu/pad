def solution():
    hours_per_person = 10
    num_people = 2

    # Calculate the total number of hours needed to solve the problem with one person working
    total_hours_single_person = hours_per_person

    # Calculate the total number of hours needed to solve the problem with two people working
    total_hours_two_people = total_hours_single_person / num_people
    result = total_hours_two_people
    return result

print(solution())