def solution():
    """Lucy works in a pet shop. She can clean 2 aquariums in 3 hours. If Lucy is working 24 hours this week, how many aquariums could she clean?"""
    # Define the rate at which Lucy can clean aquariums
    rate = 2/3  # 2 aquariums in 3 hours

    # Calculate the total number of aquariums Lucy can clean in 24 hours
    total_aquariums = rate * 24

    result = total_aquariums
    return result

print(solution())