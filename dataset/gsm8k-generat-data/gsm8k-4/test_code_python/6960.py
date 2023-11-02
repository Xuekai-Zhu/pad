def solution():
    """Jake's neighbors hire him to mow their lawn and plant some flowers. Mowing the lawn takes 1 hour and pays $15. If Jake wants to make $20/hour working for the neighbors, and planting the flowers takes 2 hours, how much should Jake charge (in total, not per hour) for planting the flowers?"""
    # Define the hourly rate and the time it takes to mow the lawn
    hourly_rate = 20
    lawn_time = 1

    # Calculate the earnings from mowing the lawn
    lawn_earnings = lawn_time * 15

    # Calculate the time it takes to plant the flowers
    flower_time = 2

    # Calculate the earnings Jake wants to make from planting flowers
    flower_earnings = flower_time * hourly_rate

    # Calculate the total earnings Jake should charge
    total_earnings = lawn_earnings + flower_earnings

    # Return the result
    result = total_earnings
    return result

print(solution())