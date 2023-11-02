def solution():
    """A store owner repacked his oils into 200 mL bottles. He was able to make 20 bottles. How many liters of oil did the store owner have?"""
    bottles = 20
    volume_per_bottle = 200
    total_volume = (bottles * volume_per_bottle) / 1000
    result = total_volume
    return result

print(solution())