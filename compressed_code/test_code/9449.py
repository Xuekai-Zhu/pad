def solution():
    
    initial_cloth = 100
    donated_cloth = 0
    for i in range(2):
        donated_cloth += initial_cloth / 2
        initial_cloth = initial_cloth / 2
    result = donated_cloth
    return result

print(solution())