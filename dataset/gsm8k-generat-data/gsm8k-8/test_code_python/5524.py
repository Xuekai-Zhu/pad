def solution():
    # Define the amount earned from repairing a phone and a laptop
    phone_earnings = 10
    laptop_earnings = 20

    # Calculate the earnings from repairing phones on Monday and Tuesday
    phone_total = (3 + 5) * phone_earnings

    # Calculate the earnings from repairing laptops on Wednesday and Thursday
    laptop_total = (2 + 4) * laptop_earnings

    # Calculate the total earnings
    total_earnings = phone_total + laptop_total
    result = total_earnings
    return result

print(solution())