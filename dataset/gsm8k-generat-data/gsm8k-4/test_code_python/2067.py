def solution():
    """A group of 6 students organized a fundraiser to go to Nicaragua for the summer. For them to go on the trip, each of them needs at least $450. On top of that, they need $3000 for their miscellaneous collective expenses. On the first day of their fundraiser, they receive $600. On the second day, they receive $900, and on the third day, they receive $400. For the next 4 days, they receive only half of what they raised on the first 3 days. How much more money does each person need to raise for them to reach their goal?"""
    # Define the total number of students
    num_students = 6

    # Define the total amount they need to raise for the trip
    trip_cost = 450 * num_students + 3000

    # Define the amount raised on the first 3 days
    first_three_days = 600 + 900 + 400

    # Define the amount raised on the next 4 days, which is half of the first 3 days
    next_four_days = (600 + 900 + 400) * 0.5 * 4

    # Calculate the total amount raised
    total_raised = first_three_days + next_four_days

    # Calculate the amount each person still needs to raise
    remaining_cost_per_person = (trip_cost - total_raised) / num_students

    # return the result
    result = remaining_cost_per_person
    return result

print(solution())