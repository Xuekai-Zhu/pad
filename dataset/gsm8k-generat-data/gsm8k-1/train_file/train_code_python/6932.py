def solution():
    """A school cafeteria uses ground mince to cook lasagnas and cottage pies. They make 100 lasagnas, which use 2 pounds of ground mince each, and cottage pies, which use 3 pounds of ground mince each. If the cafeteria has used 500 pounds of ground mince in total, how many cottage pies did they make?"""
    lasagnas = 100
    lasagna_ground_mince = 2
    cottage_pie_ground_mince = 3
    total_ground_mince = 500
    total_lasagna_ground_mince = lasagnas * lasagna_ground_mince
    total_cottage_pie_ground_mince = (total_ground_mince - total_lasagna_ground_mince)
    cottage_pies = total_cottage_pie_ground_mince / cottage_pie_ground_mince
    result = cottage_pies
    return result

print(solution())