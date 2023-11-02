def solution():
    """Care and Rick have a repair shop. Each repair is priced differently: phone repair costs $11, laptop repair costs $15 and computer repair costs $18. If they perform 5 phone repairs, 2 laptop repairs, and 2 computer repairs for this week, how much did they earn for the week?"""
    phone_price = 11
    laptop_price = 15
    computer_price = 18
    num_phone_repairs = 5
    num_laptop_repairs = 2
    num_computer_repairs = 2
    total_earnings = (phone_price * num_phone_repairs) + (laptop_price * num_laptop_repairs) + (computer_price * num_computer_repairs)
    result = total_earnings
    return result

print(solution())