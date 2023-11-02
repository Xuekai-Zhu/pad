def solution():
    
    total_money = 0
    job_money = 20 * 10
    cookie_money = 4 * 24
    lottery_money = 500 - 10
    gift_money = 500 * 2
    total_money += job_money + cookie_money + lottery_money + gift_money
    remaining_money = 5000 - total_money
    result = remaining_money
    return result

print(solution())