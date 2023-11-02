def solution():
    """Paul goes fishing every Saturday. Last week he was able to catch 5 fish for every 2 hours he was fishing. How many fish did he catch when he was fishing for 12 hours?"""
    # Define the catch rate per hour
    CATCH_RATE = 2.5

    # Calculate the number of fish caught in 12 hours
    fish_caught = CATCH_RATE * 12

    # Display the number of fish caught
    result = fish_caught
    return result

print(solution())