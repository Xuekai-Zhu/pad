def solution():
    # Calculate the total amount of money Francie receives in the first 8 weeks
    first_total = 5 * 8  # $5 allowance per week for 8 weeks

    # Calculate the total amount of money Francie receives in the next 6 weeks
    next_total = 6 * 6  # $6 allowance per week for 6 weeks

    # Calculate the total amount of money Francie has
    total_money = first_total + next_total

    # Calculate half of the total money for new clothes
    clothes_cost = total_money / 2

    # Calculate the remaining money after buying new clothes and a video game
    remaining_money = total_money - clothes_cost - 35
    result = remaining_money
    return result

print(solution())