def solution():
    """The faucet in Betsy's bathroom is broken. Every minute it drips about 10 times. What amount of water is wasted during one hour if each drop contains 0.05 mL?"""
    # Define the number of drops per minute and the volume per drop
    DROPS_PER_MINUTE = 10
    VOLUME_PER_DROP = 0.05

    # Calculate the number of drops per hour
    drops_per_hour = DROPS_PER_MINUTE * 60

    # Calculate the total volume wasted in one hour
    volume_wasted = drops_per_hour * VOLUME_PER_DROP

    # Display the total volume wasted
    result = volume_wasted
    return result

print(solution())