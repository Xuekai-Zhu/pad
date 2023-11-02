def solution():
    miles_to_overlook = 12
    miles_from_overlook = 12
    miles_per_hour_to_overlook = 4
    miles_per_hour_from_overlook = 6
    hours_to_overlook = miles_to_overlook / miles_per_hour_to_overlook
    hours_from_overlook = miles_from_overlook / miles_per_hour_from_overlook
    total_hours = hours_to_overlook + hours_from_overlook
    result = total_hours
    return result

print(solution())