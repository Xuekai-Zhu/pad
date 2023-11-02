def solution():
    
    gingerbread_sold = 10
    apple_pie_sold = 15
    sunday_gingerbread_sold = gingerbread_sold - 4
    sunday_gingerbread_earnings = gingerbread_sold + 5
    sunday_apple_pie_earnings = apple_pie_sold * 15
    total_gingerbread_earnings = gingerbread_sold * 6
    total_apple_pie_earnings = apple_pie_sold * 15
    total_earnings = total_gingerbread_earnings + total_apple_pie_earnings
    result = total_earnings
    return result

print(solution())