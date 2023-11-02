def solution():
    # Let's assume x parrots were originally perched on the tree branch
    # Then, there were also x crows perched on the tree branch
    # After an equal number of both flew away, there were (x-2) parrots and (x-2) crows left on the tree branch
    # We also know that there is 1 crow left on the tree branch, so (x-2) = 1 => x = 3
    # Therefore, there were originally 3 parrots and 3 crows perched on the tree branch
    total_birds = 6 # 3 parrots + 3 crows
    result = total_birds
    return result

print(solution())