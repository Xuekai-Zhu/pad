def solution():
    """Jake's neighbors hire him to mow their lawn and plant some flowers. Mowing the lawn takes 1 hour and pays $15. If Jake wants to make $20/hour working for the neighbors, and planting the flowers takes 2 hours, how much should Jake charge (in total, not per hour) for planting the flowers?"""
    # Calculate the earnings from mowing the lawn
    lawn_earnings = 15

    # Calculate the time required to plant the flowers
    flower_time = 2

    # Calculate the target hourly rate
    target_rate = 20

    # Calculate the earnings from planting the flowers
    flower_earnings = target_rate * flower_time

    # Calculate the total earnings
    total_earnings = lawn_earnings + flower_earnings

    # Display the total earnings
    result = flower_earnings
    return result

print(solution())