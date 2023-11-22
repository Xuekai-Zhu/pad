def solution():
    
    # Define the total number of points scored
    total_points = 251

    # Calculate the number of points scored by Naomi
    naomi_points = 68

    # Calculate the number of points scored by Yuri
    yuri_points = (naomi_points / 2) + 10

    # Calculate the number of points scored by Brianna
    brianna_points = naomi_points + 17

    # Calculate the number of points scored by Jojo
    jojo_points = total_points - naomi_points - yuri_points - brianna_points

    # Display the number of points scored by Jojo
    result = jojo_points
    return result

print(solution())