def solution():
    """Jenn is saving up money to buy a bike. She has 5 jars full of quarters. Each jar can hold 160 quarters. If the bike costs 180 dollars, how much money will she have left over after buying it?"""
    jars = 5
    quarters_per_jar = 160
    total_quarters = jars * quarters_per_jar
    total_dollars = total_quarters * 0.25
    bike_cost = 180
    leftover_money = total_dollars - bike_cost
    result = leftover_money
    return result

print(solution())