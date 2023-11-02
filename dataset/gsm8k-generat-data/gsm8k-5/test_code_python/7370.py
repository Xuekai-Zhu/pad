def solution():
    num_lessons = 20  # James gets 20 lessons
    free_lessons = 1  # James gets 1 free lesson
    paid_lessons = num_lessons - free_lessons  # James has to pay for the remaining lessons

    # Calculate the cost of the first 10 paid lessons
    cost_first_10_lessons = 10 * 5  # Each lesson costs $5
    # Calculate the cost of the remaining paid lessons
    cost_remaining_lessons = (paid_lessons - 10) * 5 * 0.5  # James gets every other lesson for free after the first 10

    # Calculate the total cost of the lessons James has to pay for
    total_cost = cost_first_10_lessons + cost_remaining_lessons

    # Calculate how much James has to pay (assuming his uncle pays for half)
    james_share = total_cost * 0.5
    result = james_share
    return result

print(solution())