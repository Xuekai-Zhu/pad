def solution():
    
    euston_carriages = 130
    norfolk_carriages = euston_carriages - 20
    norwich_carriages = 100
    flying_scotsman_carriages = norwich_carriages + 20
    total_carriages = euston_carriages + norfolk_carriages + norwich_carriages + flying_scotsman_carriages
    result = total_carriages
    return result

print(solution())