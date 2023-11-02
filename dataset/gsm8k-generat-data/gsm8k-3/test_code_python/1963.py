def solution():
    """Christine makes money by commission rate. She gets a 12% commission on all items she sells. This month, she sold $24000 worth of items. Sixty percent of all her earning will be allocated to her personal needs and the rest will be saved. How much did she save this month?"""
    # Define the commission rate and the amount of sales
    COMMISSION_RATE = 0.12
    SALES = 24000

    # Calculate Christine's earnings from sales
    earnings = COMMISSION_RATE * SALES

    # Allocate 60% of earnings to personal needs and save the rest
    personal_needs = 0.6 * earnings
    savings = earnings - personal_needs

    # Display the amount saved
    result = savings
    return result

print(solution())