def solution():
    num_students = 20
    num_teachers = 3
    ticket_price = 5

    # Calculate the total number of people going to the museum
    total_people = num_students + num_teachers

    # Calculate the total cost of entrance tickets
    total_cost = total_people * ticket_price
    result = total_cost
    return result

print(solution())