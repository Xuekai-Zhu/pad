def solution():
    """Eighteen hours ago, Beth and I took 100 photographs of our project. Today, Beth and I will take 20% fewer photographs of the same project. If we were to take 300 photographs of the project, how many photographs would we take to reach the target?"""
    # Define the initial number of photographs and the percentage decrease
    initial_photos = 100
    decrease_percentage = 20

    # Calculate the number of photos we will take today
    today_photos = initial_photos * (100 - decrease_percentage) / 100

    # Calculate the remaining number of photos we need to take
    remaining_photos = 300 - today_photos

    result = remaining_photos
    return result

print(solution())