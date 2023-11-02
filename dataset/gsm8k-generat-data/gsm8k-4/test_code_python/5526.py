def solution():
    """Jenny decided to get a cat with her girlfriend. They agreed to split all the costs down the middle except for they would each buy their own toys for the cat. The adoption fee was $50, the vet visits cost $500 for the first year and the monthly cost of food was $25. She bought $200 in toys. How much did Jenny spend on the cat in the first year?"""
    # Define the costs of adoption, vet visits, monthly food, and toys
    adoption_fee = 50
    vet_visits = 500
    monthly_food = 25
    toys = 200

    # Calculate the total cost of adoption and vet visits
    adoption_and_vet = adoption_fee + vet_visits

    # Calculate the total cost of food for the first year
    food_total = monthly_food * 12

    # Calculate the total cost for Jenny
    jenny_total = adoption_and_vet + food_total + toys

    # Calculate Jenny's half of the total cost
    jenny_share = jenny_total / 2

    result = jenny_share
    return result

print(solution())