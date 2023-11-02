def solution():
    """A team of 4 painters worked on a mansion for 3/8ths of a day every day for 3 weeks. How many hours of work did each painter put in?"""
    days_in_week = 7
    total_days = 3 * days_in_week
    hours_in_day = 24
    fraction_of_day = 3 / 8
    total_hours = total_days * hours_in_day * fraction_of_day
    num_painters = 4
    hours_per_painter = total_hours / num_painters
    result = hours_per_painter
    return result

print(solution())