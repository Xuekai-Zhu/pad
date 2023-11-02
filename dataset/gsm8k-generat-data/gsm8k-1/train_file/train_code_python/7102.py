def solution():
    """Harry decided to buy some balloons for his friend's birthday party. One balloon costs $0.5, and a pack of 10 balloons is cheaper and costs only $3. Finally, Harry wants to bring to the party exactly 14 balloons. How much did he need to pay for them?"""
    single_balloon_cost = 0.5
    pack_balloon_cost = 3
    pack_balloon_count = 10
    total_balloon_count = 14
    pack_count = total_balloon_count // pack_balloon_count
    single_count = total_balloon_count % pack_balloon_count
    total_cost = pack_count * pack_balloon_cost + single_count * single_balloon_cost
    result = total_cost
    return result

print(solution())