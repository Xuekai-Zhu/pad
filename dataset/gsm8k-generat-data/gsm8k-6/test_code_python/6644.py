def solution():
    total_hours = 157
    # Let's assume Thomas worked x hours
    x = 40  # for example purposes only.. can be any value
    toby_hours = 2*x - 10
    rebecca_hours = toby_hours - 8
    total_work_hours = x + toby_hours + rebecca_hours

    # Check if the total work hours add up to the given total
    if total_work_hours == total_hours:
        result = rebecca_hours
    else:
        result = "Invalid input - Work hours don't add up to the total"
    return result

print(solution())