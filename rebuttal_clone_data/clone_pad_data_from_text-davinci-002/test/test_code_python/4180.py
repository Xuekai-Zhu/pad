def solution():
    total_gallons = 16
    cousin_gallons = total_gallons / 2
    friend_gallons = total_gallons / 4
    initial_gallons = total_gallons - (cousin_gallons + friend_gallons)
    result = initial_gallons
    return result

print(solution())