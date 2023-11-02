def solution():
    """During a staff meeting, 50 doughnuts were served. If each of the 19 staff ate 2 doughnuts, how many doughnuts are left?"""
    # Define the total number of doughnuts served
    total_doughnuts = 50

    # Define the number of staff and the number of doughnuts eaten by each staff
    num_staff = 19
    doughnuts_per_staff = 2

    # Calculate the total number of doughnuts eaten by staff
    total_doughnuts_eaten = num_staff * doughnuts_per_staff

    # Calculate the number of doughnuts left
    doughnuts_left = total_doughnuts - total_doughnuts_eaten

    result = doughnuts_left
    return result

print(solution())