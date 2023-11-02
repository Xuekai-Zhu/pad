def solution():
    adoption_fee = 200  # dollars
    friend_contribution = 0.25 * adoption_fee  # dollars
    james_payment = adoption_fee - friend_contribution  # dollars
    result = james_payment
    return result

print(solution())