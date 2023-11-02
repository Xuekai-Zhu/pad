def solution():
    """There were 80 people at a football game on Saturday. On Monday, 20 fewer people were at the football game. On Wednesday, 50 more people were at the game than on Monday. On Friday, there were the same number of people as on Saturday and Monday combined. If their expected total audience at the football game for a week is 350, how many more people attended the games than they had expected?"""
    # Define the number of people on Saturday
    saturday = 80

    # Define the number of people on Monday
    monday = saturday - 20

    # Define the number of people on Wednesday
    wednesday = monday + 50

    # Define the number of people on Friday
    friday = saturday + monday

    # Calculate the total number of people for the week
    total = saturday + monday + wednesday + friday

    # Calculate the difference between the actual and expected total
    difference = total - 350

    result = difference
    return result

print(solution())