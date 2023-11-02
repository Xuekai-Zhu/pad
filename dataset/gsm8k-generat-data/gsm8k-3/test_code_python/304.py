def solution():
    """Carrie is wrapping three birthday presents. One present needs two square feet of wrapping paper to cover. The second present needs three-quarters of that amount. The third present needs the same amount as both other presents put together. How many square feet of wrapping paper does Carrie need for all three presents?"""
    # Calculate the amount of wrapping paper needed for the first present
    present1 = 2

    # Calculate the amount of wrapping paper needed for the second present
    present2 = 0.75 * present1

    # Calculate the total amount of wrapping paper needed for the first two presents
    total1 = present1 + present2

    # Calculate the amount of wrapping paper needed for the third present
    present3 = total1

    # Calculate the total amount of wrapping paper needed for all three presents
    total = total1 + present3

    # Display the total amount of wrapping paper needed
    result = total
    return result

print(solution())