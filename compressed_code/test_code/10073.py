def solution():
    
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