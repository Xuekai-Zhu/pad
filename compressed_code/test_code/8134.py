def solution():
    
    dozens_of_pebbles = 3
    pebbles_per_dozen = 12
    total_pebbles = dozens_of_pebbles * pebbles_per_dozen
    pebbles_per_friend = 4
    friends_received_pebbles = total_pebbles // pebbles_per_friend
    result = friends_received_pebbles
    return result

print(solution())