def solution():
    """Bobby needed to make some trips with his truck and had only 12 gallons of gasoline. He drives to a supermarket 5 miles away and then drives back home. Then he headed to his farm which was 6 miles away. Two miles into the journey, he turned around and drove back home to retrieve some farming tools he forgot to take earlier and drove down to the farm. If he now has exactly 2 gallons of gasoline left, at what rate in miles per gallon has his truck been consuming gasoline?"""
    total_distance = (5 * 2) + (6 * 2) + 2
    gas_used = 12 - 2
    mpg = total_distance / gas_used
    result = mpg
    return result

print(solution())