def solution():
    
    # Define the number of chocolate bars produced each week
    WEEKLY_BARS = 50000

    # Calculate the number of chocolate bars produced in the first week
    week1_bars = 8000

    # Calculate the number of chocolate bars produced in the second week
    week2_bars = week1_bars / 2

    # Calculate the number of chocolate bars produced in the third week
    week3_bars = week1_bars * 3

    # Calculate the total number of chocolate bars produced in the first three weeks
    total_bars = week1_bars + week2_bars + week3_bars

    # Calculate the number of chocolate bars produced in the fourth week
    week4_bars = WEEKLY_BARS - total_bars

    # Display the number of chocolate bars produced in the fourth week
    result = week4_bars
    return result

print(solution())