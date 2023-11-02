def solution():
    """A 220-liter barrel has a small leak. It lost 10% of its contents before anyone noticed. How many liters are left in the barrel?"""
    initial_volume = 220
    percent_loss = 10
    volume_remaining = initial_volume - (initial_volume * (percent_loss / 100))
    result = volume_remaining
    return result

print(solution())