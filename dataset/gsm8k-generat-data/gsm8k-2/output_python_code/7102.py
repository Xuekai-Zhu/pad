def solution():
    """Harry decided to buy some balloons for his friend's birthday party. One balloon costs $0.5, and a pack of 10 balloons is cheaper and costs only $3. Finally, Harry wants to bring to the party exactly 14 balloons. How much did he need to pay for them?"""
    single_balloon_price = 0.5
    pack_price = 3
    pack_size = 10
    total_price = 0
    full_packs = 14 // pack_size
    rest_balloons = 14 % pack_size
    total_price += full_packs * pack_price
    total_price += rest_balloons * single_balloon_price
    result = total_price
    return result

print(solution())