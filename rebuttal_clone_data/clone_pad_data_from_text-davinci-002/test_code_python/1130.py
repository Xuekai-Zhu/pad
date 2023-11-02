def solution():
 
    max_packages = 35
    total_packages = 35 + 50 + (35 / 7) + ((4 * 35) / 5)
    result = total_packages - (2 * max_packages)
    return result

print(solution())