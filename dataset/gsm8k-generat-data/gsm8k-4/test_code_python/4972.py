def solution():
    """Amanda had 7 candy bars. She gave 3 to her sister. The next day, Amanda won some prize money and bought another 30 candy bars. She gave her sister 4 times as many candy bars as she did the first time. How many candy bars did Amanda keep for herself altogether?"""
    # Define the initial number of candy bars Amanda had
    initial_candy_bars = 7

    # Define the number of candy bars Amanda gave to her sister the first time
    first_give = 3

    # Define the number of candy bars Amanda bought after winning the prize money
    second_buy = 30

    # Calculate the number of candy bars Amanda gave to her sister the second time
    second_give = first_give * 4

    # Calculate the total number of candy bars Amanda gave to her sister
    total_given = first_give + second_give

    # Calculate the total number of candy bars Amanda kept for herself
    total_kept = initial_candy_bars + second_buy - total_given

    # Return the result
    result = total_kept
    return result

print(solution())