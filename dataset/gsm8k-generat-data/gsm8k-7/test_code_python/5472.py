def solution():
    phone_price = 11
    laptop_price = 15
    computer_price = 18

    num_phone_repairs = 5
    num_laptop_repairs = 2
    num_computer_repairs = 2

    # Calculate the total earned from phone repairs
    phone_earnings = num_phone_repairs * phone_price

    # Calculate the total earned from laptop repairs
    laptop_earnings = num_laptop_repairs * laptop_price

    # Calculate the total earned from computer repairs
    computer_earnings = num_computer_repairs * computer_price

    # Calculate the total earnings for the week
    total_earnings = phone_earnings + laptop_earnings + computer_earnings
    result = total_earnings
    return result

print(solution())