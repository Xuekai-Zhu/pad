def solution():
    # Calculate the number of Easter eggs found by Hannah
    hannah_eggs = 2 * helen_eggs  
    total_eggs = hannah_eggs + helen_eggs  # total number of Easter eggs found by both Hannah and Helen
    total_eggs = 63  # total number of Easter eggs in the yard
    helen_eggs = total_eggs / 3  # assume Helen found one-third of the total
    hannah_eggs = 2 * helen_eggs  # Hannah found twice as many as Helen
    result = hannah_eggs
    return result

print(solution())