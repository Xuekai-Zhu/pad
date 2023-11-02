def solution():
    phone_repair_cost = 11  # Each phone repair costs $11
    laptop_repair_cost = 15  # Each laptop repair costs $15
    computer_repair_cost = 18  # Each computer repair costs $18
    num_phone_repairs = 5  # They performed 5 phone repairs
    num_laptop_repairs = 2  # They performed 2 laptop repairs
    num_computer_repairs = 2  # They performed 2 computer repairs

    # Calculate the total earnings for phone repairs
    phone_earnings = phone_repair_cost * num_phone_repairs

    # Calculate the total earnings for laptop repairs
    laptop_earnings = laptop_repair_cost * num_laptop_repairs

    # Calculate the total earnings for computer repairs
    computer_earnings = computer_repair_cost * num_computer_repairs

    # Calculate the total earnings for the week
    total_earnings = phone_earnings + laptop_earnings + computer_earnings
    result = total_earnings
    return result

print(solution())