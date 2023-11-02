def solution():
    """Two days ago, Uncle Welly planted 50 roses on his vacant lot. Yesterday, he planted 20 more roses than the previous day. Today, he planted twice the number of roses than two days ago. How many roses did Uncle Welly plant in his vacant lot?"""
    # Define the number of roses Uncle Welly planted two days ago
    roses_2_days_ago = 50

    # Calculate the number of roses Uncle Welly planted yesterday
    roses_yesterday = roses_2_days_ago + 20

    # Calculate the number of roses Uncle Welly planted today
    roses_today = roses_2_days_ago * 2

    # Calculate the total number of roses Uncle Welly planted
    total_roses = roses_2_days_ago + roses_yesterday + roses_today

    # Display the total number of roses planted
    result = total_roses
    return result

print(solution())