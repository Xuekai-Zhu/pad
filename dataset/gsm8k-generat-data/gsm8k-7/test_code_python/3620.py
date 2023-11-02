def solution():
    # Let x be the total capacity of the tank
    # The tank is currently 1/3 full, so 2/3 of x is empty
    # Adding 16 gallons fills the tank completely, so:
    # 2/3 of x + 16 = x
    # Solving for x:
    x = 48
    
    # Therefore the tank holds 48 gallons of water when full
    result = x
    return result

print(solution())