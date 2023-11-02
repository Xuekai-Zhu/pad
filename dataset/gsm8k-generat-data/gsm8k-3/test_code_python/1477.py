def solution():
    """Jack goes hunting 6 times a month.  The hunting season lasts for 1 quarter of the year.  He catches 2 deers each time he goes hunting and they weigh 600 pounds each.  He keeps half the weight of deer a year.  How much deer does he keep in pounds?"""
    # Define the number of times Jack goes hunting per month
    hunting_frequency = 6

    # Define the weight of each deer caught
    deer_weight = 600

    # Calculate the total weight of deer caught in a month
    monthly_deer_weight = hunting_frequency * 2 * deer_weight

    # Calculate the total weight of deer caught in a quarter
    quarterly_deer_weight = monthly_deer_weight * 3

    # Calculate the weight of deer Jack keeps each year
    yearly_kept_weight = quarterly_deer_weight / 2

    # Display the weight of deer Jack keeps each year
    result = yearly_kept_weight
    return result

print(solution())