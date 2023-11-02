def solution():
    
    long_sleeve_price = 15
    striped_price = 10
    long_sleeve_quantity = 4
    total_spent = 80
    total_long_sleeve_cost = long_sleeve_price * long_sleeve_quantity
    striped_quantity = (total_spent - total_long_sleeve_cost) / striped_price
    result = striped_quantity
    return result

print(solution())