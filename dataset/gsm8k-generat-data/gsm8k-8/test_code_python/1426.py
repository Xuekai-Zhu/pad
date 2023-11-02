def solution():
    # Calculate the total number of forms to be processed in the day
    total_forms = 2400

    # Calculate the number of forms processed per hour
    forms_per_hour = 25

    # Calculate the total number of hours needed to process all forms
    total_hours = total_forms / forms_per_hour

    # Calculate the number of clerks needed based on 8-hour work day
    clerks_needed = total_hours / 8
    result = clerks_needed
    return result

print(solution())