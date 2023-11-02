def solution():
    """Monica and Michelle are combining their money to throw a party. Monica brings $15. Michelle brings $12. The cake costs 15 dollars, and soda is $3 a bottle. Each bottle of soda has 12 servings and they buy as many bottles of soda as they can afford. If there are 8 total guests, how many servings of soda does each get?"""
    monica_money = 15
    michelle_money = 12
    total_money = monica_money + michelle_money
    soda_price = 3
    cake_price = 15
    remaining_money = total_money - cake_price
    num_bottles = remaining_money // soda_price
    num_servings = num_bottles * 12
    servings_per_guest = num_servings // 8
    result = servings_per_guest
    
    return result

print(solution())