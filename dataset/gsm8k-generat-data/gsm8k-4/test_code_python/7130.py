def solution():
    """Bethany is working at the front desk at Joe’s Gym. There were some people lifting weights when she started her shift. Then 5 more people came in and started running on the treadmill and 2 people left. There are now 19 people in the gym. How many people were lifting weights at the start of Bethany’s shift?"""
    # Define the number of people who came to the gym to lift weights when Bethany started her shift
    initial_weight_lifters = None

    # Calculate the number of people in the gym after 5 more people came in and 2 people left
    current_total = 19
    previous_total = current_total - 5 + 2

    # Calculate the number of people who were lifting weights when Bethany started her shift
    initial_weight_lifters = previous_total - initial_weight_lifters

    result = initial_weight_lifters
    return result

print(solution())