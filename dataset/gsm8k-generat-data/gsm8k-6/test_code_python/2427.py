def solution():
    # Calculate the total amount of beef sold over 3 days
    total_beef = 210 + 2*210 + 150  # sold 210 pounds on Thursday, 2*210 pounds on Friday, and 150 pounds on Saturday

    # Calculate the average amount of beef sold per day
    average_beef = total_beef / 3

    result = average_beef
    return result

print(solution())