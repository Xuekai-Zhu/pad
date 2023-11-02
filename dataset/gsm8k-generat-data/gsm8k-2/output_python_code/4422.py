def solution():
    """Monica and Michelle are combining their money to throw a party. Monica brings $15. Michelle brings $12. The cake costs 15 dollars, and soda is $3 a bottle. Each bottle of soda has 12 servings and they buy as many bottles of soda as they can afford. If there are 8 total guests, how many servings of soda does each get?"""
    monica_money = 15
    michelle_money = 12
    cake_cost = 15
    soda_cost = 3
    total_money = monica_money + michelle_money
    remaining_money = total_money - cake_cost
    soda_count = remaining_money // soda_cost
    soda_servings = soda_count * 12
    servings_per_guest = soda_servings // 8
    result = servings_per_guest
    return result

print(solution())