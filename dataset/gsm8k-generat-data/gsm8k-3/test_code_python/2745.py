def solution():
    """During a staff meeting, 50 doughnuts were served. If each of the 19 staff ate 2 doughnuts, how many doughnuts are left?"""
    # Define the number of doughnuts served
    doughnuts_served = 50

    # Define the number of staff members and the number of doughnuts each staff member ate
    num_staff = 19
    doughnuts_per_staff = 2

    # Calculate the total number of doughnuts eaten by the staff
    total_doughnuts_eaten = num_staff * doughnuts_per_staff

    # Calculate the number of doughnuts left
    doughnuts_left = doughnuts_served - total_doughnuts_eaten

    # Display the number of doughnuts left
    result = doughnuts_left
    return result

print(solution())