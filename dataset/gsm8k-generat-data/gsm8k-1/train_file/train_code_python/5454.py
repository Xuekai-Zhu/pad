def solution():
    """Hank gave his wife, Delphine, a box of 24 chocolates for Valentine's Day. On the first day, Delphine ate 4 chocolates.
    On the second day, she ate 3 less than twice as many chocolates as she ate the first day. On the third day, she ate two 
    less than the number she ate on the first day. And on the fourth day, she ate one less than she ate the previous day.
    On the fifth day, how many chocolates remained uneaten?"""

    chocolates_given = 24
    chocolates_eaten = 4
    chocolates_eaten_second_day = (2*chocolates_eaten) - 3
    chocolates_eaten_third_day = chocolates_eaten - 2
    chocolates_eaten_fourth_day = chocolates_eaten_second_day - 1
    chocolates_eaten_fifth_day = chocolates_eaten_fourth_day
    chocolates_remaining = chocolates_given - chocolates_eaten - chocolates_eaten_second_day - chocolates_eaten_third_day - chocolates_eaten_fourth_day - chocolates_eaten_fifth_day
    result = chocolates_remaining
    return result

print(solution())