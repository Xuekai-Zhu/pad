def solution():
    # Define the number of eggs needed per week
    saly_eggs = 10
    ben_eggs = 14
    ked_eggs = 0.5 * ben_eggs

    # Calculate the total number of eggs needed per month
    total_eggs = 4 * (saly_eggs + ben_eggs + ked_eggs)
    
    result = total_eggs
    return result

print(solution())