def solution():
    total_days = 5
    pb_days = 2
    cake_day = 1
    cookie_days = 4
    ham_days = total_days - pb_days - cake_day - cookie_days
    days_with_cake = cake_day + pb_days
    days_without_cake = total_days - days_with_cake
    p_cake_given_ham = cake_day / ham_days
    p_ham_given_cake = ham_days / cake_day
    p_cake_and_ham = p_cake_given_ham * p_ham_given_cake
    result = p_cake_and_ham * 100
    return result

print(solution())