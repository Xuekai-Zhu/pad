def solution():
    adults = 58 
    children = adults - 35
    seniors = children * 2
    total_guests = adults + children + seniors
    result = total_guests
    return result

print(solution())