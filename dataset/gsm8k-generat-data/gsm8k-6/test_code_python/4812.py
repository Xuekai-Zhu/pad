def solution():
    # Calculate the total number of dinners sold in 4 days
    monday_dinners = 40
    tuesday_dinners = monday_dinners + 40
    wednesday_dinners = tuesday_dinners / 2
    thursday_dinners = wednesday_dinners + 3
    total_dinners = monday_dinners + tuesday_dinners + wednesday_dinners + thursday_dinners
    result = total_dinners
    return result

print(solution())