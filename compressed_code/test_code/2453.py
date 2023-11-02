def solution():
    
    left_money = 130
    dvd_spending = 8
    remaining_money = left_money + dvd_spending
    remaining_money_proportion = 3 / 5
    after_dvds_money = remaining_money / remaining_money_proportion
    book_spending = 10
    book_proportion = 1 / 4
    initial_money = (after_dvds_money + book_spending) / (1 - book_proportion)
    result = initial_money
    return result

print(solution())