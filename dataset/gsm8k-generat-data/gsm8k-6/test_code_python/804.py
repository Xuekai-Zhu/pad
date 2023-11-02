def solution():
    # Calculate the number of panda babies born
    panda_couples = 16/2 # 16 pandas paired into mates 
    pregnant_couples = panda_couples * 0.25 # Only 25% of the panda couples get pregnant
    panda_babies = pregnant_couples * 1 # Each pregnant couple have one baby
    result = panda_babies
    return result

print(solution())