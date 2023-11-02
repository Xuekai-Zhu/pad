def solution():
    """John ends up damaging his hearing aids.  He needs to replace both of them.  They cost $2500 each. Insurance covers 80% of the cost. How much does he personally have to pay?"""
    # Define the cost of one hearing aid
    HEARING_AID_COST = 2500

    # Calculate the cost of both hearing aids
    total_cost = HEARING_AID_COST * 2

    # Calculate the amount covered by insurance
    insurance_coverage = total_cost * 0.8

    # Calculate the amount that John personally has to pay
    personal_payment = total_cost - insurance_coverage

    # Display the personal payment
    result = personal_payment
    return result

print(solution())