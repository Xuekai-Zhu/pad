def solution():
    """John is very unfit and decides to work up to doing a push-up.  He trains 5 days a week for them and starts with wall push-ups.  He adds 1 rep a day and once he gets to 15 reps he will start training high elevation push-ups. and then low elevation push-ups, and finally floor push-ups.  How many weeks will it take him to get to floor push-ups?"""
    # Define the number of reps for each type of push-up
    WALL_PUSH_UPS = 15
    HIGH_ELEVATION_PUSH_UPS = 20
    LOW_ELEVATION_PUSH_UPS = 25
    FLOOR_PUSH_UPS = 30

    # Define the number of days John trains for and his starting number of reps
    TRAINING_DAYS = 5
    starting_reps = 0

    # Initialize the number of weeks it will take John to get to floor push-ups
    weeks = 0

    # Loop until John reaches the target number of reps for floor push-ups
    while starting_reps < FLOOR_PUSH_UPS:
        # Increment the starting number of reps by 1 for each training day
        starting_reps += TRAINING_DAYS
        weeks += 1
        
        # Check if John has reached the next level of push-ups and increase his starting reps accordingly
        if starting_reps >= WALL_PUSH_UPS and starting_reps < HIGH_ELEVATION_PUSH_UPS:
            starting_reps = starting_reps + 5
        elif starting_reps >= HIGH_ELEVATION_PUSH_UPS and starting_reps < LOW_ELEVATION_PUSH_UPS:
            starting_reps = starting_reps + 5
        elif starting_reps >= LOW_ELEVATION_PUSH_UPS and starting_reps < FLOOR_PUSH_UPS:
            starting_reps = starting_reps + 5

    # Display the number of weeks it took John to get to floor push-ups
    result = weeks
    return result

print(solution())