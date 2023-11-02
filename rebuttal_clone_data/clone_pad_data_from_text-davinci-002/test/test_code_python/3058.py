def solution():
    total_sales = 1000000
    advance = 100000
    price_per_book = 2
    books_sold = total_sales - advance
    agent_percent = 10
    total_earned = books_sold * price_per_book
    agent_take = total_earned * (agent_percent / 100)
    money_kept = total_earned - agent_take
    result = money_kept
    
    return result

print(solution())