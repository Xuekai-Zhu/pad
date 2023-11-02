def solution():
    adoption_fee = 200  # The adoption fee is $200
    friend_payment = adoption_fee * 0.25  # James' friend will pay 25% of the adoption fee
    james_payment = adoption_fee - friend_payment  # James will pay the remaining amount

    result = james_payment
    return result

print(solution())