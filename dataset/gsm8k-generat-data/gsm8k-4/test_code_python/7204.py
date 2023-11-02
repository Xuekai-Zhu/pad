def solution():
    """A 4th grade class with 20 students and 3 teachers is going to a science museum. The entrance ticket costs $5 each. How much will they pay for the entrance tickets?"""
    # Define the number of students, teachers, and the ticket price
    num_students = 20
    num_teachers = 3
    ticket_price = 5

    # Calculate the total number of people going to the museum
    total_people = num_students + num_teachers

    # Calculate the total cost of the entrance tickets
    total_cost = total_people * ticket_price

    # return the result
    result = total_cost
    return result

print(solution())