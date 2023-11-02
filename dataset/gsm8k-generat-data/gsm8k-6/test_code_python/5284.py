def solution():
    # Calculate the total number of eggs Kelly's chickens produce in 4 weeks
    total_eggs = 8 * 3 * 7 * 4  # 8 chickens, 3 eggs each per day, 7 days in a week, 4 weeks
    dozens_of_eggs = total_eggs / 12  # convert to dozens
    money_made = dozens_of_eggs * 5  # $5 per dozen
    result = money_made
    return result

print(solution())