def solution():
    """Harry is a professional dog-walker.  He is paid to go on long walks with dogs while their families are away from home.  On Monday, Wednesday, and Friday, Harry walks 7 dogs.  On Tuesday, he walks 12 dogs.  And on Thursday he walks 9 dogs.  He is paid $5 for each dog that he walks.  How many dollars does Harry earn in a week?"""
    # Calculate the number of dogs Harry walks each week
    dogs_walked = 7 * 3 + 12 + 9

    # Calculate Harry's weekly earnings
    earnings = dogs_walked * 5

    # Display Harry's earnings
    result = earnings
    return result

print(solution())