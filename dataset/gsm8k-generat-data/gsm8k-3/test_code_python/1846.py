def solution():
    """Bob and Kate went to a restaurant for dinner. After they were done eating the waitress gave a $30 bill to Bob and a $25 bill to Kate, but told them they were eligible for special discounts; 5% for Bob, 2% for Kate. Considering the discounts, how much do they have to pay in total?"""
    # Define the initial bills for Bob and Kate
    bob_bill = 30
    kate_bill = 25

    # Calculate the discount amounts for Bob and Kate
    bob_discount = 0.05 * bob_bill
    kate_discount = 0.02 * kate_bill

    # Calculate the final bills for Bob and Kate after discount
    bob_final = bob_bill - bob_discount
    kate_final = kate_bill - kate_discount

    # Calculate the total bill including both Bob and Kate's bills after discount
    total_bill = bob_final + kate_final

    # Display the total bill
    result = total_bill
    return result

print(solution())