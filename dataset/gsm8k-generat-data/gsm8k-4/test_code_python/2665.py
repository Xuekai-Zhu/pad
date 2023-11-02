def solution():
    """Paul goes fishing every Saturday. Last week he was able to catch 5 fish for every 2 hours he was fishing. How many fish did he catch when he was fishing for 12 hours?"""
    # Define the catch rate of fish per hour
    catch_rate = 5 / 2

    # Calculate the total number of fish caught in 12 hours
    total_catch = catch_rate * 12

    # return the result
    result = total_catch
    return result

print(solution())