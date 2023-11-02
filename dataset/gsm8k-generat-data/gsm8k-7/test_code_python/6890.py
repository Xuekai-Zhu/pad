def solution():
    chris_sword = 15
    jam_sword = 3 + 2*chris_sword
    jun_sword = 5 + jam_sword
    
    # Calculate the difference in length between June's sword and Christopher's sword
    dif_in_length = jun_sword - chris_sword
    
    result = dif_in_length
    return result

print(solution())