def solution():
    """Carla's teacher tells her that she needs to collect 30 leaves and 20 bugs for a project that's due in 10 days. How many items does Carla need to collect each day if she always wants to collect the same daily amount?"""
    # Define the number of leaves and bugs Carla needs to collect
    num_leaves = 30
    num_bugs = 20

    # Define the number of days Carla has to complete the project
    num_days = 10

    # Calculate the total number of items Carla needs to collect
    total_items = num_leaves + num_bugs

    # Calculate the daily amount Carla needs to collect
    daily_amount = total_items / num_days

    # Round up to ensure Carla collects enough items each day
    daily_amount = math.ceil(daily_amount)

    # Display the daily amount Carla needs to collect
    result = daily_amount
    return result

print(solution())