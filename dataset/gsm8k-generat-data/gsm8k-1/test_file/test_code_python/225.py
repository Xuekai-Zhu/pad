def solution():
    """A watermelon farm produced 120 baby watermelons. Ashlyn went to the farm after two months and found out that 30% of the watermelons were ready for harvest, so she took them home. When she came back two weeks later, 3/4 of the remaining melons were ready, so she harvested them. How many melons were not ready to be harvested after the two weeks?"""
    total_watermelons = 120
    ready_first_time = total_watermelons * 0.3
    remaining_watermelons = total_watermelons - ready_first_time
    ready_second_time = remaining_watermelons * 0.75
    not_ready_second_time = remaining_watermelons - ready_second_time
    result = not_ready_second_time
    return result

print(solution())