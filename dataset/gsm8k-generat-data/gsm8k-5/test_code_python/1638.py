def solution():
    total_savings_needed = 108000  # The downpayment for the house
    years_to_save = 3  # The time it will take to save enough for the downpayment
    months_to_save = years_to_save * 12  # Convert to months

    # Calculate the total amount to be saved each month by both Richard and Sarah
    total_monthly_savings = total_savings_needed / months_to_save

    # Divide the monthly savings equally between Richard and Sarah
    savings_per_person = total_monthly_savings / 2
    result = savings_per_person
    return result

print(solution())