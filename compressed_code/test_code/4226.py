def solution():
    
    phone_repair_price = 11
    laptop_repair_price = 15
    computer_repair_price = 18
    total_phone_repairs = 5
    total_laptop_repairs = 2
    total_computer_repairs = 2
    total_earnings = (phone_repair_price * total_phone_repairs) + (laptop_repair_price * total_laptop_repairs) + (computer_repair_price * total_computer_repairs)
    result = total_earnings
    return result

print(solution())