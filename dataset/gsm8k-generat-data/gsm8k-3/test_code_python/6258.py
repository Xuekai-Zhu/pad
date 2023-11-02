def solution():
    """Jordan has a new hit song on Spotify. 3 months are left in the year, and she currently has 60,000 listens. If the number of listens per month doubles, how many listens will the song have by the end of the year?"""
    # Define the current number of listens and the remaining number of months
    current_listens = 60000
    remaining_months = 3

    # Double the number of listens per month for the remaining months
    total_listens = current_listens * (2 ** remaining_months)

    # Display the total number of listens at the end of the year
    result = total_listens
    return result

print(solution())