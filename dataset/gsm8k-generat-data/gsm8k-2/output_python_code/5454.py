def solution():
    """Hank gave his wife, Delphine, a box of 24 chocolates for Valentine's Day. On the first day, Delphine ate 4 chocolates. On the second day, she ate 3 less than twice as many chocolates as she ate the first day. On the third day, she ate two less than the number she ate on the first day. And on the fourth day, she ate one less than she ate the previous day. On the fifth day, how many chocolates remained uneaten?"""
    total_chocolates = 24
    delphine_ate = 4
    delphine_ate_second_day = 2 * (delphine_ate) - 3
    delphine_ate_third_day = delphine_ate - 2
    delphine_ate_fourth_day = delphine_ate_second_day - 1
    chocolates_remaining = total_chocolates - delphine_ate - delphine_ate_second_day - delphine_ate_third_day - delphine_ate_fourth_day
    result = chocolates_remaining
    return result

print(solution())