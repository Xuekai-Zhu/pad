def solution():
    """A patient is receiving treatment through a saline drip which makes 20 drops per minute. If the treatment lasts 2 hours, and every 100 drops equal 5 ml of liquid, how many milliliters of treatment will the patient receive after the 2 hours have passed?"""
    drops_per_minute = 20
    minutes_per_hour = 60
    treatment_time = 2 # hours
    drops_per_hour = drops_per_minute * minutes_per_hour
    total_drops = drops_per_hour * treatment_time
    ml_per_100_drops = 5
    ml_received = (total_drops/100) * ml_per_100_drops
    result = ml_received
    return result

print(solution())