def solution():
    """Gabby is saving money to buy a new makeup set. The makeup set costs $65 and she already has $35. Gabby’s mom gives her an additional $20. How much money does Gabby need to buy the set?"""
    # Define the cost of the makeup set and the amount of money Gabby has
    COST_MAKEUP_SET = 65
    MONEY_GABBY_HAS = 35

    # Define the amount of money Gabby's mom gives her
    MONEY_GABBY_MOM_GIVES = 20

    # Calculate the total amount of money Gabby has
    total_money = MONEY_GABBY_HAS + MONEY_GABBY_MOM_GIVES

    # Calculate the amount of money Gabby needs to buy the makeup set
    money_needed = COST_MAKEUP_SET - total_money

    # Display the amount of money Gabby needs
    result = money_needed
    return result

print(solution())