def solution():
    check_amount = 200  
    tip_percentage = 0.2  
    tip_amount = check_amount * tip_percentage  # calculate tip amount
    total_amount = check_amount + tip_amount + 10  # add check amount, tip amount, and friend's contribution
    mark_should_add = total_amount - check_amount - 10  # amount that Mark should add
    result = mark_should_add
    return result

print(solution())