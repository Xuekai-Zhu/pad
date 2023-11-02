def solution():
    drops_per_minute = 20  # The saline drip makes 20 drops per minute
    minutes = 120  # The treatment lasts 2 hours
    total_drops = drops_per_minute * minutes  # Calculate the total number of drops

    ml_per_100_drops = 5  # Every 100 drops equal 5 ml of liquid
    total_ml = (total_drops / 100) * ml_per_100_drops  # Calculate the total number of ml of treatment

    result = total_ml
    return result

print(solution())