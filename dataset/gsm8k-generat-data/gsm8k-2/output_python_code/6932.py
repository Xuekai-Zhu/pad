def solution():
    """A school cafeteria uses ground mince to cook lasagnas and cottage pies. They make 100 lasagnas, which use 2 pounds of ground mince each, and cottage pies, which use 3 pounds of ground mince each. If the cafeteria has used 500 pounds of ground mince in total, how many cottage pies did they make?"""
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