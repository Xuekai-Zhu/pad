def solution():
    """Two days ago, Uncle Welly planted 50 roses on his vacant lot. Yesterday, he planted 20 more roses than the previous day. Today, he planted twice the number of roses than two days ago. How many roses did Uncle Welly plant in his vacant lot?"""
    # Define the initial number of roses planted
    initial_roses = 50

    # Calculate the number of roses planted yesterday
    yesterday_roses = initial_roses + 20

    # Calculate the number of roses planted today
    today_roses = initial_roses * 2

    # Calculate the total number of roses planted
    total_roses = initial_roses + yesterday_roses + today_roses

    result = total_roses
    return result

print(solution())