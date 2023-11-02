def solution():
    
    lasagnas = 100
    lasagna_minced = 2
    cottage_minced = 3
    total_minced = 500
    minced_used_for_lasagnas = lasagnas * lasagna_minced
    minced_used_for_cottage_pies = total_minced - minced_used_for_lasagnas
    cottage_pies = minced_used_for_cottage_pies / cottage_minced
    result = cottage_pies
    return result

print(solution())