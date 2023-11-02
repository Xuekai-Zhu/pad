def solution():
    """Seven parrots and some crows are perched on a tree branch. There was a noise and the same number of parrots and crows flew away. If only 2 parrots and 1 crow are left on the tree branch now, how many birds were perched on the branch to begin with?"""
    # Let's assume the number of crows and parrots to be x each at the start
    # Total number of birds = 2x + 2x = 4x (since equal number of crows and parrots)
    # If same number of crows and parrots flew away, the remaining number of birds is (x-1) each of crows and parrots
    # Remaining number of birds = 2(x-1) + 1 = 2x - 1
    # Given that 2 parrots and 1 crow are left on the branch
    # Therefore, (x-1) = 2 and (x-1) = 1
    # Solving these equations, we get x = 3
    # Therefore, the initial number of birds on the branch was 4x = 4*3 = 12
    
    result = 12
    return result

print(solution())