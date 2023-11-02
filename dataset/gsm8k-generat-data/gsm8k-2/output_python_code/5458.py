def solution():
    """The bus driver drives an average of 2 hours each day, 5 days a week. From Monday to Wednesday he drove at an average speed of 12 kilometers per hour, and from Thursday to Friday at an average speed of 9 kilometers per hour. How many kilometers did the driver travel during these 5 days?"""
    days = 5
    hours_per_day = 2
    total_hours = days * hours_per_day
    monday_to_wednesday_speed = 12
    thursday_to_friday_speed = 9
    monday_to_wednesday_distance = monday_to_wednesday_speed * total_hours * 3
    thursday_to_friday_distance = thursday_to_friday_speed * total_hours * 2
    total_distance = monday_to_wednesday_distance + thursday_to_friday_distance
    result = total_distance
    return result

print(solution())