def solution():
    # Calculate the remaining amount to be paid
    remaining_amount = 13380 - 5400  # Mr. Dubois paid $5400 initially
    months_to_pay = remaining_amount / 420  # Mr. Dubois pays $420 every month
    result = months_to_pay
    return result

print(solution())