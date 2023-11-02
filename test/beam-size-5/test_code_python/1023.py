def solution():
    
    package1_price = 3
    package2_price = 6
    package3_price = 6
    package1_num_sandwiches = 2
    package2_num_sandwiches = 4
    package3_num_sandwiches = 8
    total_price = (package1_price * package1_num_sandwiches) + (package2_price * package2_num_sandwiches) + (package3_price * package3_num_sandwiches)
    price_of_8_sandwiches = total_price - (package1_num_sandwiches + package2_num_sandwiches + package3_num_sandwiches)
    result = price_of_8_sandwiches
    return result

print(solution())