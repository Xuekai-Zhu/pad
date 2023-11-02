def solution():
    # Define the adoption fee and the friend's contribution
    adoption_fee = 200
    friend_contribution = 0.25 * adoption_fee

    # Calculate how much James has to pay
    james_payment = adoption_fee - friend_contribution
    result = james_payment
    return result

print(solution())