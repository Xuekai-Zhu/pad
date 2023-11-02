def solution():
    """There were 80 people at a football game on Saturday. On Monday, 20 fewer people were at the football game. On Wednesday, 50 more people were at the game than on Monday. On Friday, there were the same number of people as on Saturday and Monday combined. If their expected total audience at the football game for a week is 350, how many more people attended the games than they had expected?"""
    # Define the number of attendees for each day of the week
    SATURDAY_ATTENDEES = 80
    MONDAY_ATTENDEES = SATURDAY_ATTENDEES - 20
    WEDNESDAY_ATTENDEES = MONDAY_ATTENDEES + 50
    FRIDAY_ATTENDEES = SATURDAY_ATTENDEES + MONDAY_ATTENDEES

    # Calculate the total number of attendees for the week
    total_attendees = SATURDAY_ATTENDEES + MONDAY_ATTENDEES + WEDNESDAY_ATTENDEES + FRIDAY_ATTENDEES

    # Calculate the number of attendees more than expected
    more_attendees = total_attendees - 350

    # Display the number of attendees more than expected
    result = more_attendees
    return result

print(solution())