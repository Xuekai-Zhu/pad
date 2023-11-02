def solution():
    """A patient is receiving treatment through a saline drip which makes 20 drops per minute. If the treatment lasts 2 hours, and every 100 drops equal 5 ml of liquid, how many milliliters of treatment will the patient receive after the 2 hours have passed?"""
    # Define the number of drops per minute and the conversion factor from drops to ml
    DROPS_PER_MINUTE = 20
    DROPS_PER_ML = 100 / 5

    # Define the duration of the treatment in minutes
    duration_minutes = 2 * 60

    # Calculate the total number of drops the patient will receive
    total_drops = duration_minutes * DROPS_PER_MINUTE

    # Convert the total number of drops to milliliters of treatment
    total_ml = total_drops / DROPS_PER_ML

    # Display the total amount of treatment in milliliters
    result = total_ml
    return result

print(solution())