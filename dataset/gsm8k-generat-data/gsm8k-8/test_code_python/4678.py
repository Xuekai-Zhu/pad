def solution():
    # Calculate the number of people who attended the second showing
    num_people_second_showing = 3 * 200

    # Calculate the total number of people who attended both showings
    total_num_people = 200 + num_people_second_showing

    # Calculate the total revenue from ticket sales
    total_revenue = total_num_people * 25

    result = total_revenue
    return result

print(solution())