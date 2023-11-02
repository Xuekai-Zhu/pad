def solution():
    christmas_date = 25
    possible_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    # Check which day of the week Christmas falls on in a non-leap year
    christmas_day = possible_days[(24 + 5 * ((6 - 1) % 4)) % 7]
    if christmas_day == "Sunday":
        result = "yes"
    else:
        result = "no"
    return result

print(solution())