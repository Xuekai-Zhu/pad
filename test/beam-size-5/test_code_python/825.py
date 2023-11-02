def solution():
    
    # Define the total number of bars of chocolate produced in a month
    TOTAL_BARS = 50000

    # Define the number of bars of chocolate produced in the first week
    week1_bars = 8000

    # Define the number of bars of chocolate produced in the second week
    week2_bars = week1_bars / 2

    # Define the number of bars of chocolate produced in the third week
    week3_bars = week1_bars * 3

    # Calculate the total number of bars of chocolate produced
    total_bars = week1_bars + week2_bars + week3_bars

    # Calculate the bars of chocolate produced in the fourth week
    week4_bars = total_bars - total_bars

    # Display the bars of chocolate produced in the fourth week
    result = week4_bars
    return result

print(solution())