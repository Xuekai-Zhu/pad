def solution():
    target_savings = 75  # Edmund needs to save up $75
    base_pay = 2  # Edmund earns $2 for every extra chore he does
    total_chores = 12 * 2  # Edmund has to do 12 chores per week, and he is doing this for two weeks
    extra_chores = total_chores - 12 * 7  # Edmund is doing 4 extra chores per day for two weeks, so he is doing 56 chores in total
    extra_pay = extra_chores * base_pay  # Edmund earns $2 for every extra chore he does
    total_earnings = extra_pay  # Edmund only earns money from doing extra chores

    result = total_earnings
    return result

print(solution())