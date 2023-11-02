def solution():
    
    budget = 50
    tshirt_price = 8
    bag_price = 10
    keychain_price = 2/3
    total_spent = (2*tshirt_price) + (2*bag_price)
    budget_left = budget - total_spent
    keychains_bought = budget_left // keychain_price
    result = keychains_bought
    return result

print(solution())