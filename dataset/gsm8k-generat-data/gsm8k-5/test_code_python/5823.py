def solution():
    drops_per_minute = 10  # The faucet drips 10 times per minute
    drops_per_hour = drops_per_minute * 60  # Convert drops per minute to drops per hour
    volume_per_drop = 0.05  # Each drop contains 0.05 mL of water

    # Calculate the total volume of water wasted in one hour
    total_volume = drops_per_hour * volume_per_drop

    result = total_volume
    return result

print(solution())