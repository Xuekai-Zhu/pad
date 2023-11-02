def solution():
    # Calculate the total allowance that Carol receives in 10 weeks
    total_allowance = 20 * 10

    # Calculate the extra money that Carol earns from doing chores in 10 weeks
    extra_money = 1.5 * x * 10

    # Calculate the total money that Carol has at the end of 10 weeks
    total_money = total_allowance + extra_money

    # Calculate the average number of extra chores that Carol did each week
    avg_extra_chores = x

    # Solve for x using the equation total_money = 425
    x = (425 - total_allowance) / (1.5 * 10)

    result = avg_extra_chores
    return result

print(solution())