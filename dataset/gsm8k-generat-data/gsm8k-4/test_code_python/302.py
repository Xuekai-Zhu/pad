def solution():
    """Carrie is wrapping three birthday presents. One present needs two square feet of wrapping paper to cover. The second present needs three-quarters of that amount. The third present needs the same amount as both other presents put together. How many square feet of wrapping paper does Carrie need for all three presents?"""
    # Define the area of the first present
    present1_area = 2

    # Calculate the area of the second present
    present2_area = present1_area * 0.75

    # Calculate the total area of the first two presents
    present12_area = present1_area + present2_area

    # Calculate the area of the third present
    present3_area = present12_area

    # Calculate the total area of wrapping paper needed
    total_area = present1_area + present2_area + present3_area

    # return the result
    result = total_area
    return result

print(solution())