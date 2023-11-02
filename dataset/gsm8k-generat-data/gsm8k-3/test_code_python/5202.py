def solution():
    """The snack machine at Richmond High School sells candy bars for $2 each and chips for $.50 each. How much money, in dollars, will 5 students need in total if each of them gets 1 candy bar and 2 bags of chips?"""
    # Define the prices of candy bars and chips
    CANDY_PRICE = 2
    CHIP_PRICE = 0.5

    # Define the number of candy bars and bags of chips each student gets
    candy_bars_per_student = 1
    chips_per_student = 2

    # Define the number of students
    num_students = 5

    # Calculate the total cost for each student
    cost_per_student = (candy_bars_per_student * CANDY_PRICE) + (chips_per_student * CHIP_PRICE)

    # Calculate the total cost for all the students
    total_cost = cost_per_student * num_students

    # Display the total cost
    result = total_cost
    return result

print(solution())