def solution():
    
    candy_price = 5
    orange_price = 10
    orange_count = 20
    goal = 1000
    orange_sales = orange_price * orange_count
    remaining_goal = goal - orange_sales
    candy_count = remaining_goal // candy_price
    result = candy_count
    return result

print(solution())