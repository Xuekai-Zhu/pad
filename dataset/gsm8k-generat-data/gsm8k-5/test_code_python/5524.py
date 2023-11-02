def solution():
    # Calculate Gondor's earnings from repairing phones
    phones_earnings = (3 + 5) * 10  # Gondor repaired 3 phones on Monday and 5 phones on Tuesday, and he earns $10 per phone

    # Calculate Gondor's earnings from repairing laptops
    laptops_earnings = (2 + 4) * 20  # Gondor repaired 2 laptops on Wednesday and 4 laptops on Thursday, and he earns $20 per laptop

    # Calculate Gondor's total earnings
    total_earnings = phones_earnings + laptops_earnings
    result = total_earnings
    return result

print(solution())