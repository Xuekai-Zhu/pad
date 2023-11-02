def solution():
    monday_sales = 40  # The restaurant sold 40 dinners on Monday
    tuesday_sales = monday_sales + 40  # The restaurant sold 40 more dinners on Tuesday than Monday
    wednesday_sales = tuesday_sales / 2  # The restaurant sold half the amount of dinners on Wednesday as it did on Tuesday
    thursday_sales = wednesday_sales + 3  # The restaurant sold 3 more dinners on Thursday than on Wednesday

    # Calculate the total number of dinners sold in the 4 days
    total_sales = monday_sales + tuesday_sales + wednesday_sales + thursday_sales
    result = total_sales
    return result

print(solution())