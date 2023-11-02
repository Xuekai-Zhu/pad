def solution():
    # Calculate the total amount earned from extra chores over 10 weeks
    extra_earnings = 425 - (20 * 10) # total earnings minus fixed allowance
    num_extra_chores = extra_earnings/1.5 # calculate the number of extra chores completed
    average_extra_chores = num_extra_chores/10 # calculate the average number of extra chores completed each week
    result = average_extra_chores
    return result

print(solution())