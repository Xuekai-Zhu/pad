def solution():
    total_floors = 20  # Elevator needs to move down 20 floors
    first_half_floors = 10  # Elevator takes 15 minutes to travel down first half floors
    next_five_floors = 5  # Elevator takes 5 minutes per floor to travel down next 5 floors
    final_five_floors = 16  # Elevator takes 16 minutes per floor to travel down final 5 floors

    # Calculate the total time for elevator to move down the first half of the floors
    first_half_time = 15

    # Calculate the total time for elevator to move down the next 5 floors
    next_five_time = 5 * next_five_floors

    # Calculate the total time for elevator to move down the final 5 floors
    final_five_time = 16 * final_five_floors

    # Calculate the total time for elevator to reach the bottom floor
    total_time = first_half_time + next_five_time + final_five_time
    total_time_in_hours = total_time / 60  # Convert total_time from minutes to hours
    result = total_time_in_hours
    return result

print(solution())