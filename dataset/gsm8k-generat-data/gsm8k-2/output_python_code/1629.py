def solution():
    """A cobbler can mend 3 pairs of shoes in an hour. From Monday to Thursday, the cobbler works for 8 hours each day, and on Friday, he only works from 8am to 11am. How many pairs of shoes can the cobbler mend in a week?"""
    shoes_per_hour = 3
    total_week_hours = (8 * 4) + 3 # 3 hours on Friday morning
    total_shoes = shoes_per_hour * total_week_hours
    result = total_shoes
    return result

print(solution())