def solution():
    """The faucet in Betsy's bathroom is broken. Every minute it drips about 10 times. What amount of water is wasted during one hour if each drop contains 0.05 mL?"""
    drops_per_minute = 10
    minutes_per_hour = 60
    volume_per_drop = 0.05
    wasted_volume = drops_per_minute * minutes_per_hour * volume_per_drop
    result = wasted_volume
    return result

print(solution())