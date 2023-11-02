def solution():
    """Four runners ran a combined total of 195 miles last week. Katarina ran 51 miles. Tomas, Tyler, and Harriet all ran the same distance. How many miles did Harriet run?"""
    # Define the total distance and Katarina's distance
    total_distance = 195
    katarina_distance = 51

    # Calculate the combined distance of Tomas, Tyler, and Harriet
    combined_distance = total_distance - katarina_distance

    # Divide the combined distance by 3 to get each person's distance
    harriet_distance = combined_distance / 3

    # Display Harriet's distance
    result = harriet_distance
    return result

print(solution())