def solution():
    """An aqua park charges $12 admission and $6 for a tour. A group of 10 people goes to the aquarium and takes the tour; while a group of 5 people only goes to the aquarium. How much does the aqua park earn?"""
    # Define the prices of admission and tour
    ADMISSION_PRICE = 12
    TOUR_PRICE = 6

    # Calculate the earnings from the group of 10
    group_10_total = ADMISSION_PRICE * 10 + TOUR_PRICE * 10

    # Calculate the earnings from the group of 5
    group_5_total = ADMISSION_PRICE * 5

    # Calculate the total earnings
    total_earnings = group_10_total + group_5_total

    # Display the total earnings
    result = total_earnings
    return result

print(solution())