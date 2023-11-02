def solution():
    """Gondor is a technician, he earns $10 from repairing a phone and $20 from repairing a laptop. If he was able to repair 3 phones last Monday, 5 phones last Tuesday, 2 laptops on Wednesday, and 4 laptops last Thursday, how much does he earn in total?"""
    # Define the prices for repairing a phone and a laptop
    PHONE_PRICE = 10
    LAPTOP_PRICE = 20

    # Calculate the earnings for repairing phones
    phone_earnings = (3 + 5) * PHONE_PRICE

    # Calculate the earnings for repairing laptops
    laptop_earnings = (2 + 4) * LAPTOP_PRICE

    # Calculate the total earnings
    total_earnings = phone_earnings + laptop_earnings

    # Return the result
    result = total_earnings
    return result

print(solution())