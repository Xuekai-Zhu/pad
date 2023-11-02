def solution():
    phone_repair = 10
    laptop_repair = 20

    num_phones_mon = 3
    num_phones_tue = 5
    num_laptops_wed = 2
    num_laptops_thu = 4

    # Calculate the total earning from phone repairs
    total_phone_earnings = (num_phones_mon + num_phones_tue) * phone_repair

    # Calculate the total earning from laptop repairs
    total_laptop_earnings = (num_laptops_wed + num_laptops_thu) * laptop_repair

    # Calculate the total earning from both phone and laptop repairs
    total_earnings = total_phone_earnings + total_laptop_earnings
    result = total_earnings
    return result

print(solution())