def solution():
    """Pete walks backwards three times faster than Susan walks forwards, and Tracy does one-handed cartwheels twice as fast as Susan walks forwards. But Pete can walk on his hands only one quarter the speed that Tracy can do cartwheels. If Pete walks on his hands at 2 miles per hour, how fast can Pete walk backwards, in miles per hour?"""
    # Let's assume Susan's walking rate is x miles per hour
    susans_rate = 1

    # Pete walks backwards three times faster than Susan walks forwards
    petes_backwards_rate = 3 * susans_rate

    # Tracy does one-handed cartwheels twice as fast as Susan walks forwards
    tracys_rate = 2 * susans_rate

    # Pete can walk on his hands only one quarter the speed that Tracy can do cartwheels, at 2 miles per hour
    petes_handwalking_rate = 0.25 * tracys_rate

    # Pete's total rate, accounting for both handwalking and backward walking
    petes_total_rate = petes_handwalking_rate + petes_backwards_rate

    result = petes_backwards_rate
    return result

print(solution())