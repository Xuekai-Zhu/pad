def solution():
    monthly_charge = 140
    first_half_charge = monthly_charge * 2
    second_half_charge = first_half_charge * 0.9

    # Calculate the total amount charged for the first half of the year
    first_half_total = first_half_charge + first_half_charge

    # Calculate the total amount charged for the second half of the year
    second_half_total = second_half_charge * 2

    # Calculate the total amount charged for the entire year
    total_charge = first_half_total + second_half_total
    result = total_charge
    return result

print(solution())