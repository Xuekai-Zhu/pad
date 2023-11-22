def solution():
    
    # Define the total number of members
    total_members = 52

    # Calculate the number of boys and girls
    boys = total_members * 0.5
    girls = total_members * 0.5

    # Calculate the number of people who can't make it to the show
    non_busy = (total_members - boys - girls) / 2

    # Calculate the number of people who sang
    sing = total_members - 3 - non_busy

    # Display the number of people who sang
    result = sing
    return result

print(solution())