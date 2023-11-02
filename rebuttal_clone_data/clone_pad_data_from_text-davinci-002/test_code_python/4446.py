def solution():
    total_people = 12
    adults = total_people - 2
    children = 2
    reservation_fee = 20
    adult_fee = 3
    child_fee = 1
    total_fee = reservation_fee + (adults * adult_fee) + (children * child_fee)
    result = total_fee
    return result

print(solution())