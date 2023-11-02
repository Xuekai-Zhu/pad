def solution():
    
    bread_cost = 50
    ham_cost = 150
    total_cost = bread_cost + ham_cost + 200
    combined_cost = bread_cost + ham_cost
    percent = (combined_cost/total_cost) * 100
    result = percent
    return result

print(solution())