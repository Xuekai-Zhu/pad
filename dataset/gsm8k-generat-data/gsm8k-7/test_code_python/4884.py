def solution():
    adoption_fee = 200
    friend_payment = adoption_fee * 0.25  # 25% of adoption fee
    james_payment = adoption_fee - friend_payment
    result = james_payment
    return result

print(solution())