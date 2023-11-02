def solution():
    # Calculate the total number of drops received over 2 hours
    total_drops = 20 * 60 * 2  # the saline drip makes 20 drops per minute, and the treatment lasts for 2 hours

    # Calculate the total number of milliliters received
    total_ml = (total_drops / 100) * 5  # every 100 drops equal 5 ml of liquid

    result = total_ml
    return result

print(solution())