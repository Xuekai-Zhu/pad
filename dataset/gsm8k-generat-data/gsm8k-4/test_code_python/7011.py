def solution():
    """The number of elephants at Gestures For Good park is 3 times as many as the number of elephants at We Preserve For Future park. If there are 70 elephants at We Preserve For Future, calculate the total number of elephants in the two parks."""
    # Define the number of elephants at We Preserve For Future park
    elephants_we_preserve = 70

    # Calculate the number of elephants at Gestures For Good park
    elephants_gestures = 3 * elephants_we_preserve

    # Calculate the total number of elephants
    total_elephants = elephants_gestures + elephants_we_preserve

    # return the result
    result = total_elephants
    return result

print(solution())