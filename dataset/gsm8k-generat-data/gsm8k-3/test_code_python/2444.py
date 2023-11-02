def solution():
    """The school decided to have a fundraiser to collect $750 for new basketball equipment. Families could donate $25, $50, or $100. Families who donated $25 got Bronze Status. Families who donated $50 got Silver Status. Families who donated $100 got Gold Status. With one day left in the fundraiser, the school has 10 Bronze Status families, 7 Silver Status Families and 1 Gold Status family. How much do they need to raise on the final day to reach their goal?"""
    # Define the donation amounts and corresponding status
    BRONZE_AMOUNT = 25
    SILVER_AMOUNT = 50
    GOLD_AMOUNT = 100

    # Define the number of families in each status
    bronze_families = 10
    silver_families = 7
    gold_families = 1

    # Calculate the total amount raised so far
    total_amount = bronze_families * BRONZE_AMOUNT + silver_families * SILVER_AMOUNT + gold_families * GOLD_AMOUNT

    # Calculate the amount still needed
    amount_needed = 750 - total_amount

    # Display the amount still needed
    result = amount_needed
    return result

print(solution())