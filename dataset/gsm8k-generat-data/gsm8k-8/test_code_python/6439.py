def solution():
    # Define the initial number of push-ups and the number of days in a week
    starting_pushups = 10
    days_in_week = 7

    # Calculate the total number of push-ups after 7 days
    total_pushups = starting_pushups + (starting_pushups + 5) + (starting_pushups + 10) + (starting_pushups + 15) + (starting_pushups + 20) + (starting_pushups + 25) + (starting_pushups + 30)

    # Return the result
    result = total_pushups
    return result

print(solution())