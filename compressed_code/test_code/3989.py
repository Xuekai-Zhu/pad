def solution():
    
    forks = 6
    knives = forks + 9
    spoons = 2 * knives
    teaspoons = forks / 2
    total_cutlery = forks + knives + spoons + teaspoons
    total_cutlery += 2 * 4 
    result = total_cutlery
    return result

print(solution())