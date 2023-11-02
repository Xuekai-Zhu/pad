def solution():
    """James decides to buy two suits. The first is an off-the-rack suit which costs $300. The second is a tailored suit that costs three as much plus an extra $200 for tailoring. How much did he pay for both suits?"""
    off_the_rack_price = 300
    tailored_price = 3 * off_the_rack_price + 200
    total_price = off_the_rack_price + tailored_price
    result = total_price
    return result

print(solution())