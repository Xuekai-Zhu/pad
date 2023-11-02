def solution():
    """A school cafeteria uses ground mince to cook lasagnas and cottage pies. They make 100 lasagnas, which use 2 pounds of ground mince each,
    and cottage pies, which use 3 pounds of ground mince each. If the cafeteria has used 500 pounds of ground mince in total, how many
    cottage pies did they make?"""
    # Define the number of lasagnas and the amount of mince used per lasagna
    lasagnas = 100
    lasagna_mince = 2

    # Define the amount of mince used for cottage pies
    pie_mince = 3

    # Calculate the total amount of mince used for lasagnas
    total_lasagna_mince = lasagnas * lasagna_mince

    # Calculate the amount of mince used for cottage pies
    pie_mince_used = 500 - total_lasagna_mince

    # Calculate the number of cottage pies made
    pies = pie_mince_used // pie_mince

    result = pies
    return result

print(solution())