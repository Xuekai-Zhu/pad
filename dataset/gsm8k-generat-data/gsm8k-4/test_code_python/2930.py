def solution():
    """An aqua park charges $12 admission and $6 for a tour. A group of 10 people goes to the aquarium and takes the tour; while a group of 5 people only goes to the aquarium. How much does the aqua park earn?"""
    # Define the prices of admission and tour
    admission_price = 12
    tour_price = 6

    # Calculate the earnings from the first group
    group1_earnings = (admission_price + tour_price) * 10

    # Calculate the earnings from the second group
    group2_earnings = admission_price * 5

    # Calculate the total earnings
    total_earnings = group1_earnings + group2_earnings

    # return the result
    result = total_earnings
    return result

print(solution())