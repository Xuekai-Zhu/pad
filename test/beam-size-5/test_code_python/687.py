def solution():
    num_vaccines = 2
    vaccine_price = 20
    heartworm_check_percentage = 0.6
    total_bill = num_vaccines * vaccine_price

    heartworm_check_amount = total_bill * heartworm_check_percentage
    heartworm_check_amount = total_bill * heartworm_check_amount

    money_left = 125 - heartworm_check_amount
    result = money_left
    return result

print(solution())