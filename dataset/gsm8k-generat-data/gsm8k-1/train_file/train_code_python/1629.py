def solution():
    """A cobbler can mend 3 pairs of shoes in an hour. From Monday to Thursday, the cobbler works for 8 hours each day, and on Friday, he only works from 8am to 11am. How many pairs of shoes can the cobbler mend in a week?"""
    pairs_per_hour = 3
    work_hours_mon_thurs = 4 * 8
    work_hours_fri = 3
    total_work_hours = work_hours_mon_thurs + work_hours_fri
    total_pairs = total_work_hours * pairs_per_hour
    result = total_pairs
    return result

print(solution())