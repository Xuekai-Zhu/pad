def solution():
    adoption_fee = 200
    friend_percent = 25
    friend_fee = adoption_fee * (friend_percent / 100)
    james_fee = adoption_fee - friend_fee
    result = james_fee
    return result

print(solution())