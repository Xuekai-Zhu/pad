def solution():
    
    initial_nickels = 5
    final_nickels = 2
    gum_per_nickel = 2
    nickels_used = initial_nickels - final_nickels
    gum_received = nickels_used * gum_per_nickel
    result = gum_received
    return result

print(solution())