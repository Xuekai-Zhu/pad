def solution():
    """Miriam is trying to exercise more and figures if she counts her exercises it will be encouraging to see her numbers go up. On Monday she does 5 push-ups. On Tuesday she does 7 push-ups. On Wednesday she does twice as many push-ups as the day before. On Thursday she does half the number of total pushups she already did that week. Finally, on Friday she does as many pushups as the total number she did over the previous four days. How many pushups does Miriam do on Friday?"""
    # Define the number of push-ups for each day
    monday_pushups = 5
    tuesday_pushups = 7
    wednesday_pushups = 2 * tuesday_pushups
    thursday_pushups = (monday_pushups + tuesday_pushups + wednesday_pushups) / 2
    friday_pushups = monday_pushups + tuesday_pushups + wednesday_pushups + thursday_pushups

    # Display the number of push-ups on Friday
    result = friday_pushups
    return result

print(solution())