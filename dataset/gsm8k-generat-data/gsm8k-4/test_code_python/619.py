def solution():
    """Harry is a professional dog-walker.  He is paid to go on long walks with dogs while their families are away from home.  On Monday, Wednesday, and Friday, Harry walks 7 dogs.  On Tuesday, he walks 12 dogs.  And on Thursday he walks 9 dogs.  He is paid $5 for each dog that he walks.  How many dollars does Harry earn in a week?"""
    # Define the number of dogs walked on each day
    monday_dogs = 7
    tuesday_dogs = 12
    wednesday_dogs = 7
    thursday_dogs = 9
    friday_dogs = 7

    # Calculate the total number of dogs walked in a week
    total_dogs = monday_dogs + tuesday_dogs + wednesday_dogs + thursday_dogs + friday_dogs

    # Calculate Harry's earnings for the week
    earnings = total_dogs * 5

    # return the result
    result = earnings
    return result

print(solution())