def solution():
    """During a fundraiser, each of the 20 members of a group sold candy bars which costs $0.50 each. If each member sold an average of 8 candy bars, how much money did they earn from their candy bars sales, in dollars?"""
    num_members = 20
    candy_price = 0.5
    avg_candy_bars_per_member = 8
    total_candy_bars_sold = num_members * avg_candy_bars_per_member
    total_earnings = total_candy_bars_sold * candy_price
    result = total_earnings
    return result

print(solution())