def solution():
    """There is a lot of dust in Susie's house. It takes her 2 hours to vacuum the whole house. She can vacuum each room in 20 minutes. How many rooms does she have in her house?"""
    # Convert 2 hours to minutes
    total_minutes = 2 * 60

    # Calculate the number of rooms Susie can vacuum in total
    num_rooms = total_minutes // 20

    # Display the number of rooms
    result = num_rooms
    return result

print(solution())