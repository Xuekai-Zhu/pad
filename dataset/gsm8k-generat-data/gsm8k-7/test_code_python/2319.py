def solution():
    buying_price = 1000   # buying price of one dog
    profit_percentage = 0.3   # 30% profit

    selling_price = buying_price + (buying_price * profit_percentage)   # selling price of one dog
    friend_buying_two = selling_price * 2   # total cost for two dogs

    result = friend_buying_two
    return result

print(solution())