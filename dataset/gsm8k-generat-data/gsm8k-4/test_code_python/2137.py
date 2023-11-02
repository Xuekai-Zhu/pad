def solution():
    """In his garden, Grandpa had counted 36 small tomatoes before going on vacation. When he came back from vacation, he counted 100 times more tomatoes. How many tomatoes grew in his absence?"""
    # Define the initial number of tomatoes
    initial_tomatoes = 36

    # Calculate the number of tomatoes after Grandpa came back from vacation
    final_tomatoes = initial_tomatoes * 100

    # Calculate the number of tomatoes that grew in Grandpa's absence
    growth = final_tomatoes - initial_tomatoes

    # Return the result
    result = growth
    return result

print(solution())