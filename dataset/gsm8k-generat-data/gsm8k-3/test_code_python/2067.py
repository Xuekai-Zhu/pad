def solution():
    """A group of 6 students organized a fundraiser to go to Nicaragua for the summer. For them to go on the trip, each of them needs at least $450. On top of that, they need $3000 for their miscellaneous collective expenses. On the first day of their fundraiser, they receive $600. On the second day, they receive $900, and on the third day, they receive $400. For the next 4 days, they receive only half of what they raised on the first 3 days. How much more money does each person need to raise for them to reach their goal?"""
    # Define the minimum amount each student needs to raise
    MINIMUM_AMOUNT = 450

    # Define the number of students and miscellaneous expenses
    num_students = 6
    misc_expenses = 3000

    # Define the amounts raised each day
    day1 = 600
    day2 = 900
    day3 = 400
    day4 = day1/2
    day5 = day2/2
    day6 = day3/2
    day7 = day4/2
    day8 = day5/2
    day9 = day6/2
    day10 = day7/2
    day11 = day8/2
    day12 = day9/2
    day13 = day10/2
    day14 = day11/2
    day15 = day12/2
    day16 = day13/2
    day17 = day14/2
    day18 = day15/2
    day19 = day16/2
    day20 = day17/2

    # Calculate the total amount raised
    total_raised = day1 + day2 + day3 + day4 + day5 + day6 + day7 + day8 + day9 + day10 + day11 + day12 + day13 + day14 + day15 + day16 + day17 + day18 + day19 + day20

    # Calculate the total amount needed for the trip
    total_needed = MINIMUM_AMOUNT * num_students + misc_expenses

    # Calculate the amount each student still needs to raise
    amount_remaining = total_needed - total_raised
    amount_per_student = amount_remaining / num_students

    # Display the amount each student needs to raise
    result = amount_per_student
    return result

print(solution())