def solution():
    
    bread_cost = 50
    ham_cost = 150
    total_cost = bread_cost + ham_cost + 200
    ham_and_bread_cost = bread_cost + ham_cost
    percent = (ham_and_bread_cost / total_cost) * 100
    result = percent
    return result

print(solution())