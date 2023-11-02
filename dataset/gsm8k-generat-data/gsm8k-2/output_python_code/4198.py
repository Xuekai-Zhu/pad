def solution():
    """Jenn is saving up money to buy a bike. She has 5 jars full of quarters. Each jar can hold 160 quarters. If the bike costs 180 dollars, how much money will she have left over after buying it?"""
    jar_capacity = 160
    num_jars = 5
    total_quarters = jar_capacity * num_jars
    bike_cost = 180
    quarters_needed = bike_cost * 4
    quarters_left_over = total_quarters - quarters_needed
    dollars_left_over = quarters_left_over / 4
    result = dollars_left_over
    return result

print(solution())