def solution():
    # Calculate earnings from Monday appointments
    monday_earnings = 5 * 1.5 * 20

    # Calculate earnings from Tuesday appointment
    tuesday_earnings = 3 * 20

    # Calculate earnings from Thursday appointments
    thursday_earnings = 2 * 2 * 20

    # Calculate earnings from Saturday appointment
    saturday_earnings = 6 * 20

    # Calculate total earnings for the week
    total_earnings = monday_earnings + tuesday_earnings + thursday_earnings + saturday_earnings

    result = total_earnings
    return result

print(solution())