def solution():
    
    # Define the number of cups of feed per chicken
    CUPS_PER_CHICKEN = 3

    # Define the number of meals Wendi has
    NUM_MEALS = 3

    # Define the number of cups of feed Wendi gives each meal
    MORNING_FEED = 15
    AFTERNOON_FEED = 25

    # Calculate the total number of cups of feed Wendi gives to her meals
    total_feed = MORNING_FEED + AFTERNOON_FEED

    # Calculate the number of cups of feed Wendi needs to give her chickens in the final meal
    final_meal_feed = NUM_MEALS * CUPS_PER_CHICKEN

    # Display the number of cups of feed Wendi needs to give her chickens in the final meal
    result = final_meal_feed
    return result

print(solution())