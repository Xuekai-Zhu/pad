def solution():
    # Calculate the final population after all the changes
    population = 300000  # starting population
    population += 50000  # 50,000 people immigrate
    population -= 30000  # 30,000 people leave
    pregnant = population // 8  # 1/8 of the population gets pregnant
    twins = pregnant // 4  # 1/4 of pregnant people have twins
    population += twins  # add the number of twins born to the population
    result = population
    return result

print(solution())