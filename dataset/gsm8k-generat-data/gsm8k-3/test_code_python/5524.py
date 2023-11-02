def solution():
    """Gondor is a technician, he earns $10 from repairing a phone and $20 from repairing a laptop. If he was able to repair 3 phones last Monday, 5 phones last Tuesday, 2 laptops on Wednesday, and 4 laptops last Thursday, how much does he earn in total?"""
    # Define the price of repairing a phone and a laptop
    PHONE_PRICE = 10
    LAPTOP_PRICE = 20

    # Define the number of phones and laptops repaired each day
    monday_phones = 3
    tuesday_phones = 5
    wednesday_laptops = 2
    thursday_laptops = 4

    # Calculate the total earnings
    total_earnings = (monday_phones + tuesday_phones) * PHONE_PRICE + (wednesday_laptops + thursday_laptops) * LAPTOP_PRICE

    # Display the total earnings
    result = total_earnings
    return result

print(solution())