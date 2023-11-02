def solution():
    """Kim's dad would buy her 2 candy bars a week.  She would eat 1 candy bar every 4 weeks, saving the rest.  After 16 weeks, how many candy bars did Kim have saved?"""
    # Define the number of candy bars Kim's dad would buy her per week
    CANDY_BARS_PER_WEEK = 2

    # Calculate the total number of candy bars Kim would have eaten in 16 weeks
    candy_bars_eaten = 16 // 4

    # Calculate the total number of candy bars Kim would have saved in 16 weeks
    candy_bars_saved = (16 * CANDY_BARS_PER_WEEK) - candy_bars_eaten

    # Display the total number of candy bars Kim saved
    result = candy_bars_saved
    return result

print(solution())