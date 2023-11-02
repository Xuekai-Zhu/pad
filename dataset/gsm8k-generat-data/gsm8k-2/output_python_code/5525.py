def solution():
    """Jenny decided to get a cat with her girlfriend. They agreed to split all the costs down the middle except for they would each buy their own toys for the cat. The adoption fee was $50, the vet visits cost $500 for the first year and the monthly cost of food was $25. She bought $200 in toys. How much did Jenny spend on the cat in the first year?"""
    adoption_fee = 50
    vet_visits = 500
    food_cost = 25 * 12
    jenny_toys = 200
    total_cost = adoption_fee + vet_visits + food_cost + jenny_toys
    jenny_share = (total_cost - jenny_toys) / 2
    result = jenny_share + jenny_toys
    return result

print(solution())