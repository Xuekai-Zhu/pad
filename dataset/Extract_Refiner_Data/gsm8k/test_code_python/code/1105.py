def solution():
    
    # Define the number of women and the heights of the women wearing in inches
    total_women = 3
    women_height_4 = 3
    women_height_2 = 3

    # Calculate the total height of the women wearing in inches
    total_height_inches = women_height_4 * 4 + women_height_2 * 2

    # Calculate the average height of the women at the party
    avg_height = total_height_inches / total_women

    # Display the average height
    result = avg_height
    return result

print(solution())