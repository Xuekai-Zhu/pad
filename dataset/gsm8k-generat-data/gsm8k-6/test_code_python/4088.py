def solution():
    # Calculate Bill's pay for the first 40 hours of work
    pay_40_hours = 20 * 40  # Bill gets paid $20 every hour up to 40 hours

    # Calculate Bill's pay for the remaining 10 hours of work
    extra_hours = 10
    pay_extra_hours = 2 * 20 * extra_hours  # Bill gets paid double for every hour worked over 40

    # Calculate Bill's total pay for the week
    total_pay = pay_40_hours + pay_extra_hours

    result = total_pay
    return result

print(solution())