def solution():
    screens_in_march = 8800  # Bennett sold 8800 window screens in March
    screens_in_february = screens_in_march / 4  # Bennett sold a fourth of what he sold in March in February
    screens_last_month = screens_in_february / 2  # Bennett sold twice as many window screens in February as he sold last month

    # Calculate the total number of screens sold from January to March
    total_screens_sold = screens_last_month + screens_in_february + screens_in_march
    result = total_screens_sold
    return result

print(solution())