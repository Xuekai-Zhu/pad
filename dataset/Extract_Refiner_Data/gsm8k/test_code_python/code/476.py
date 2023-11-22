def solution():
    
    # Define the number of tubes of blue paint Ben has
    ben_blue_paint = 4

    # Define the number of tubes of yellow paint Ben has
    ben_yellow_paint = 3

    # Calculate the number of tubes of blue paint Jasper has
    jasper_blue_paint = ben_blue_paint / 2

    # Calculate the number of tubes of yellow paint Jasper has
    jasper_yellow_paint = ben_yellow_paint * 3

    # Calculate the total number of tubes of paint Jasper has
    total_paint = jasper_blue_paint + jasper_yellow_paint

    # Display the total number of tubes of paint Jasper has
    result = total_paint
    return result

print(solution())