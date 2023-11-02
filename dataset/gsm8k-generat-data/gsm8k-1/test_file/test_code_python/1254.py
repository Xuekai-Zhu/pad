def solution():
    """There are five phones on a phone plan. The main phone costs twice as much as each additional phone. If the main phone plan costs $20, how much does the whole phone plan cost?"""
    main_phone_cost = 20
    additional_phone_cost = main_phone_cost / 2
    total_cost = main_phone_cost + (additional_phone_cost * 4)
    result = total_cost
    return result

Note: This solution assumes that there are four additional phones, as the question states there are five phones on the plan in total.

print(solution())