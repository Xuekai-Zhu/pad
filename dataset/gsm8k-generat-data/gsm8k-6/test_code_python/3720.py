def solution():
    # Calculate the total number of pastries sold in a week
    total_sales = sum(range(2, 9))  # sales start at 2 on Monday and increase by 1 each day
    average_sales = total_sales / 7  # divide by 7 days in a week to find average

    result = average_sales
    return result

print(solution())