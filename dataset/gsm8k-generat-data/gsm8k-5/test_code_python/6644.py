def solution():
    total_hours = 157  # Total hours worked by all three

    # Hours worked by Thomas
    x = 54  # Example input
    hours_thomas = x

    # Hours worked by Toby
    hours_toby = 2*x - 10

    # Hours worked by Rebecca
    hours_rebecca = hours_toby - 8

    # Check if the total hours match
    if hours_thomas + hours_toby + hours_rebecca == total_hours:
        result = hours_rebecca
    else:
        result = "Error: Total hours do not match"
    return result

print(solution())