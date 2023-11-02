def solution():
    starting_amount = 80  # Bob started out the week with $80
    monday_spending = starting_amount / 2  # Bob spent half of the starting amount on Monday
    monday_amount_left = starting_amount - monday_spending  # Bob has this much left after Monday

    tuesday_spending = monday_amount_left / 5  # Bob spent one-fifth of the amount left from Monday on Tuesday
    tuesday_amount_left = monday_amount_left - tuesday_spending  # Bob has this much left after Tuesday

    wednesday_spending = (3/8) * tuesday_amount_left  # Bob spent 3/8ths of the amount left from Tuesday on Wednesday
    remaining_amount = tuesday_amount_left - wednesday_spending  # Bob has this much left now

    result = remaining_amount
    return result

print(solution())