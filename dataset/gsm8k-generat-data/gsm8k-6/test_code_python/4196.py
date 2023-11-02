def solution():
    # Calculate the number of fertile eggs
    fertile_eggs = 30 - (30 * 0.2)  # 20 percent of the eggs are infertile
 
    # Calculate the number of eggs that will hatch
    hatching_eggs = fertile_eggs - (fertile_eggs / 3)  # a third of the fertile eggs won't hatch due to calcification issues
 
    result = hatching_eggs
    return result

print(solution())