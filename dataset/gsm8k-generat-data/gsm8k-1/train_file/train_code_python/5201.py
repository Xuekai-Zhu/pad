def solution():
    """The snack machine at Richmond High School sells candy bars for $2 each and chips for $.50 each. How much money, in dollars, will 5 students need in total if each of them gets 1 candy bar and 2 bags of chips?"""
    candy_bar_price = 2
    chip_price = 0.5
    num_students = 5
    candy_bars_per_student = 1
    chips_per_student = 2
    total_cost = (candy_bar_price * candy_bars_per_student + chip_price * chips_per_student) * num_students
    result = total_cost
    return result

print(solution())