def solution():
    """On Thursday Walmart sold 210 pounds of ground beef. On Friday they sold twice that amount. On Saturday they only sold 150 pounds.  What was the average amount of beef sold per day?"""
    # Calculate the total amount of beef sold
    total_beef = 210 + 2 * 210 + 150

    # Calculate the average amount of beef sold per day
    average_beef = total_beef / 3

    # Display the average amount of beef sold per day
    result = average_beef
    return result

print(solution())