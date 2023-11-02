def solution():
    # Find the total number of tires on the friend's cycles
    friend_tires = 3 * (4) + 1 + 3  # friend has 3 times as many tires as Ignatius's bikes, plus a unicycle and a tricycle
    
    # Find the number of bicycles that the friend owns
    bikes = (friend_tires - 1 - 3) / 2  # subtract tires of unicycle and tricycle from friend's total tires, then divide remaining by 2 (tires per bike)
    result = bikes
    return result

print(solution())