def solution():
    # Determine if New Year's Day always falls on a Wednesday
    year = 2021 # any year can be used here
    day_of_week = "Sunday" # January 1st, 2021 was on a Friday
    
    # Calculate the day of the week for New Year's Day of the next seven years
    for i in range(1, 8):
        year += 1
        if year % 4 == 0:
            day_of_week = "Thursday" if day_of_week == "Wednesday" else "Wednesday"
        else:
            day_of_week = "Wednesday" if day_of_week == "Thursday" else "Thursday"
    
    # Check if New Year's Day always falls on a Wednesday
    if day_of_week == "Wednesday":
        result = "yes"
    else:
        result = "no"
    return result

print(solution())