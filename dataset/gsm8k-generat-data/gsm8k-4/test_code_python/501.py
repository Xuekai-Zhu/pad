def solution():
    """John is very unfit and decides to work up to doing a push-up. He trains 5 days a week for them and starts with wall push-ups. He adds 1 rep a day and once he gets to 15 reps he will start training high elevation push-ups. and then low elevation push-ups, and finally floor push-ups. How many weeks will it take him to get to floor push-ups?"""
    # Define the starting number of push-ups, the maximum number of push-ups to reach, and the number of push-ups to add each day
    starting_pushups = 0
    max_pushups = 15
    pushups_added_per_day = 1

    # Define the push-up types and the number of push-ups required for each type
    pushup_types = ["wall", "high elevation", "low elevation", "floor"]
    pushups_required = [max_pushups, max_pushups, max_pushups, max_pushups]

    # Define the training days per week
    training_days = 5

    # Initialize the week counter and the current push-up type
    weeks = 0
    current_pushup_type = 0

    # Keep training until all push-up types have been completed
    while current_pushup_type < len(pushup_types):
        # Increment the week counter
        weeks += 1
        
        # Increment the number of push-ups for the current push-up type
        pushups_required[current_pushup_type] -= (pushups_added_per_day * training_days)
        
        # If the current push-up type has been completed, move on to the next one
        if pushups_required[current_pushup_type] <= 0:
            current_pushup_type += 1
            
    # return the number of weeks it took to complete all push-up types
    result = weeks
    return result

print(solution())