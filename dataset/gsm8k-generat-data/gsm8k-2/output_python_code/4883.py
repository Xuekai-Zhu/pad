def solution():
    """James goes to pet smart to adopt a puppy. The adoption fee is $200 and his friend agrees to pay 25% of that. How much does James have to pay?"""
    adoption_fee = 200
    friend_contribution = 0.25 * adoption_fee
    james_payment = adoption_fee - friend_contribution
    result = james_payment
    return result

print(solution())