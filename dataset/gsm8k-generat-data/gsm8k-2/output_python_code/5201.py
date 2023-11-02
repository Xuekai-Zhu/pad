def solution():
    """The snack machine at Richmond High School sells candy bars for $2 each and chips for $0.50 each. How much money, in dollars, will 5 students need in total if each of them gets 1 candy bar and 2 bags of chips?"""
    candy_price = 2
    chips_price = 0.5
    num_students = 5
    num_candy_bars = num_students
    num_chips_bags = 2 * num_students
    total_cost = num_candy_bars * candy_price + num_chips_bags * chips_price
    result = total_cost
    return result

print(solution())