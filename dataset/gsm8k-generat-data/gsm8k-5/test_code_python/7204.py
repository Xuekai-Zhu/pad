def solution():
    num_students = 20  # There are 20 students in the 4th grade class
    num_teachers = 3  # There are 3 teachers accompanying the class
    total_people = num_students + num_teachers  # Total number of people going to the museum
    ticket_price = 5  # The entrance ticket costs $5 each

    # Calculate the total cost for entrance tickets
    total_cost = total_people * ticket_price
    result = total_cost
    return result

print(solution())