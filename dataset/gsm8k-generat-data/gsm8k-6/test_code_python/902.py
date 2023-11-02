def solution():
    # Find the number of straws Troy fed to the adult pigs
    adult_pig_straws = (3/5) * 300  

    # Find the total number of straws fed to both adult pigs and piglets
    total_straws = adult_pig_straws + 20  

    # Find the number of straws each piglet ate
    straw_per_piglet = total_straws / 20  
    result = straw_per_piglet
    return result

print(solution())