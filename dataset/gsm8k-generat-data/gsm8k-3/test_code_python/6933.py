def solution():
    """A school cafeteria uses ground mince to cook lasagnas and cottage pies. They make 100 lasagnas,
    which use 2 pounds of ground mince each, and cottage pies, which use 3 pounds of ground mince each.
    If the cafeteria has used 500 pounds of ground mince in total, how many cottage pies did they make?"""
    # Calculate the total used mince for lasagnas
    lasagnas_mince = 100 * 2

    # Calculate the total used mince for cottage pies
    cottage_pies_mince = (500 - lasagnas_mince) / 3

    # Display the number of cottage pies made
    result = int(cottage_pies_mince)
    return result

print(solution())