def solution():
    """Bob and Kate went to a restaurant for dinner. After they were done eating the waitress gave a $30 bill to Bob and a $25 bill to Kate, but told them they were eligible for special discounts; 5% for Bob, 2% for Kate. Considering the discounts, how much do they have to pay in total?"""
    # Define the initial bills for Bob and Kate
    bob_bill = 30
    kate_bill = 25

    # Calculate the discount for Bob and Kate
    bob_discount = bob_bill * 0.05
    kate_discount = kate_bill * 0.02

    # Calculate the total savings for Bob and Kate
    total_savings = bob_discount + kate_discount

    # Calculate the total bill after the discount
    total_bill = bob_bill + kate_bill - total_savings

    # Return the result
    result = total_bill
    return result

print(solution())