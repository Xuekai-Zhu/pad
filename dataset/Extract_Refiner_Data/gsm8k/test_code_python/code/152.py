def solution():
    
    monkey_bananas = 200
    gorilla_bananas = 400
    baboon_bananas = 100
    total_bananas_needed = monkey_bananas + gorilla_bananas + baboon_bananas
    bananas_per_month = total_bananas_needed / 2
    result = bananas_per_month
    return result

print(solution())