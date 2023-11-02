def solution():
    wednesdays_in_year = 52
    total_hours_on_wednesdays = 1248
    old_testament_hours = 52
    new_testament_hours = 18
    total_hours_to_read_bible = (old_testament_hours + new_testament_hours) * 15
    if total_hours_to_read_bible <= total_hours_on_wednesdays:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())