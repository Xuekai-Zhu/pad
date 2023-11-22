def solution():
    
    # Define the distance run by Aaron and Vanessa
    aaron_distance = 4
    vanessa_distance = aaron_distance * 2

    # Define the time taken by Aaron to complete his part of the race
    aaron_time = 16

    # Calculate the distance run by Vanessa
    vanessa_distance = vanessa_distance / 2

    # Calculate the time taken by Vanessa to complete his part of the race
    vanessa_time = vanessa_distance / vanessa_speed

    # Display the time taken by Vanessa to complete her part of the race
    result = vanessa_time
    return result

print(solution())