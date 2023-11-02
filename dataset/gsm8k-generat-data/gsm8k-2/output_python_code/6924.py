def solution():
    """A patient is receiving treatment through a saline drip which makes 20 drops per minute. If the treatment lasts 2 hours, and every 100 drops equal 5 ml of liquid, how many milliliters of treatment will the patient receive after the 2 hours have passed?"""
    drops_per_minute = 20
    drops_per_hour = drops_per_minute * 60
    total_drops = drops_per_hour * 2
    ml_per_100_drops = 5
    total_ml = (total_drops // 100) * ml_per_100_drops
    result = total_ml
    return result

print(solution())