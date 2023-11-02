def solution():
    """A patient is receiving treatment through a saline drip which makes 20 drops per minute. If the treatment lasts 2 hours, and every 100 drops equal 5 ml of liquid, how many milliliters of treatment will the patient receive after the 2 hours have passed?"""
    # Define the number of drops per minute and the duration of the treatment in minutes
    drops_per_minute = 20
    treatment_duration = 120

    # Calculate the total number of drops received during the treatment
    total_drops = drops_per_minute * treatment_duration

    # Calculate the total volume of liquid received in ml
    total_ml = (total_drops / 100) * 5

    result = total_ml
    return result

print(solution())