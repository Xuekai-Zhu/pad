def solution():
    """Carla's teacher tells her that she needs to collect 30 leaves and 20 bugs for a project that's due in 10 days. How many items does Carla need to collect each day if she always wants to collect the same daily amount?"""
    # Define the number of leaves and bugs required and the number of days to complete the project
    leaves_required = 30
    bugs_required = 20
    days = 10

    # Calculate the total number of leaves and bugs needed
    total_items = leaves_required + bugs_required

    # Calculate the number of items needed to be collected each day
    daily_items = total_items / days

    # Round up to ensure Carla has enough items by the deadline
    daily_items = round(daily_items + 0.5)

    # Return the result
    result = daily_items
    return result

print(solution())