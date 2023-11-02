def solution():
    
    adoption_fee = 200
    friend_contribution = 0.25 * adoption_fee
    james_payment = adoption_fee - friend_contribution
    result = james_payment
    return result

print(solution())