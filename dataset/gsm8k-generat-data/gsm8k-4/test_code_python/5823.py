def solution():
    """The faucet in Betsy's bathroom is broken. Every minute it drips about 10 times. What amount of water is wasted during one hour if each drop contains 0.05 mL?"""
    # Define the number of drops per minute and the volume per drop
    drops_per_min = 10
    volume_per_drop = 0.05

    # Calculate the volume wasted per minute
    volume_per_min = drops_per_min * volume_per_drop

    # Calculate the volume wasted per hour
    volume_per_hour = volume_per_min * 60

    # Round the result to two decimal places and return
    result = round(volume_per_hour, 2)
    return result

print(solution())