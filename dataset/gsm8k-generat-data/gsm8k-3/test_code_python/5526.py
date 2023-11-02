def solution():
    """Jenny decided to get a cat with her girlfriend.  They agreed to split all the costs down the middle except for they would each buy their own toys for the cat.  The adoption fee was $50, the vet visits cost $500 for the first year and the monthly cost of food was $25.  She bought $200 in toys.  How much did Jenny spend on the cat in the first year?"""
    # Define the cost of adoption, vet visits, monthly food, and toys
    ADOPTION_FEE = 50
    VET_VISITS_COST = 500
    MONTHLY_FOOD_COST = 25

    # Get the cost of Jenny's toys
    TOY_COST = 200

    # Calculate the total cost of vet visits for the first year
    total_vet_visits_cost = VET_VISITS_COST

    # Calculate the total cost of food for the first year
    total_food_cost = MONTHLY_FOOD_COST * 12

    # Calculate the total cost for Jenny
    jenny_cost = (ADOPTION_FEE + total_vet_visits_cost + total_food_cost + TOY_COST) / 2

    # Display Jenny's total cost
    result = jenny_cost
    return result

print(solution())