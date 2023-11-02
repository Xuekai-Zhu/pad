def solution():
    """Bobby needed to make some trips with his truck and had only 12 gallons of gasoline. He drives to a supermarket 5 miles away and then drives back home. Then he headed to his farm which was 6 miles away. Two miles into the journey, he turned around and drove back home to retrieve some farming tools he forgot to take earlier and drove down to the farm. If he now has exactly 2 gallons of gasoline left, at what rate in miles per gallon has his truck been consuming gasoline?"""
    # Define the distances traveled
    distance1 = 5 * 2 # distance to the supermarket (round-trip)
    distance2 = 6 * 2 # distance to the farm (round-trip)

    # Define the amount of gas used
    gas_used = 12 - 2 # 2 gallons of gas left after the last trip

    # Calculate the rate of gasoline consumption
    rate = (distance1 + distance2) / gas_used

    # Display the rate of gasoline consumption
    result = rate
    return result

print(solution())