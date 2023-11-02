def solution():
    week1_sales = 50  # The fishmonger sold 50 kg of salmon in the first week
    week2_sales = 3 * week1_sales  # He sold three times more in the second week than the first

    # Calculate the total sales in two weeks
    total_sales = week1_sales + week2_sales
    result = total_sales
    return result

print(solution())