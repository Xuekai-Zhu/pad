def solution():
    
    # Define the number of puffs of clouds counted on Monday
    monday_clouds = 3

    # Calculate the number of puffs of clouds counted on Tuesday
    tuesday_clouds = monday_clouds * 2

    # Calculate the number of puffs of clouds counted on Wednesday
    wednesday_clouds = tuesday_clouds * 2

    # Calculate the total number of puffs of clouds counted over the week
    total_clouds = monday_clouds + tuesday_clouds + wednesday_clouds + (2 * tuesday_clouds)

    # Display the total number of puffs of clouds counted
    result = total_clouds
    return result

print(solution())