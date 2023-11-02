def solution():
    """At his cafe, Milton sells apple pie and peach pie slices. He cuts the apple pie into 8 slices. He cuts the peach pie into 6 slices. On the weekend, 56 customers ordered apple pie slices and 48 customers ordered peach pie slices. How many pies did Milton sell during the weekend?"""
    apple_slices_per_pie = 8
    peach_slices_per_pie = 6
    total_apple_slices = 56
    total_peach_slices = 48
    total_pies = (total_apple_slices // apple_slices_per_pie) + (total_peach_slices // peach_slices_per_pie)
    result = total_pies
    return result

print(solution())