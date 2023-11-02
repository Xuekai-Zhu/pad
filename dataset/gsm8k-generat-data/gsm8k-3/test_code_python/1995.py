def solution():
    """Eighteen hours ago, Beth and I took 100 photographs of our project. Today, Beth and I will take 20% fewer photographs of the same project. If we were to take 300 photographs of the project, how many photographs would we take to reach the target?"""
    # Define the original number of photographs taken
    initial_photos = 100

    # Calculate the new number of photographs with a 20% reduction
    reduced_photos = initial_photos * 0.8

    # Calculate the number of additional photographs needed to reach the target
    additional_photos = 300 - reduced_photos

    # Display the number of additional photographs needed
    result = additional_photos
    return result

print(solution())