def solution():
    """During a fundraiser, each of the 20 members of a group sold candy bars which costs $0.50 each. If each member sold an average of 8 candy bars, how much money did they earn from their candy bars sales, in dollars?"""
    num_members = 20
    candy_bar_cost = 0.5
    candy_bars_per_member = 8
    total_candy_bars = num_members * candy_bars_per_member
    total_sales = total_candy_bars * candy_bar_cost
    result = total_sales
    return result

print(solution())