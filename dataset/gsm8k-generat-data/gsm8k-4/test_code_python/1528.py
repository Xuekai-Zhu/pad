def solution():
    """Gabby is saving money to buy a new makeup set. The makeup set costs $65 and she already has $35. Gabby’s mom gives her an additional $20. How much money does Gabby need to buy the set?"""
    # Define the cost of the makeup set and the amount Gabby already has
    MAKEUP_COST = 65
    GABBY_SAVINGS = 35

    # Define the amount Gabby's mom gives her
    MOM_GIFT = 20

    # Calculate the total amount Gabby has
    total_savings = GABBY_SAVINGS + MOM_GIFT

    # Calculate the remaining amount needed to buy the makeup set
    remaining_cost = MAKEUP_COST - total_savings

    # Return the result
    result = remaining_cost
    return result

print(solution())