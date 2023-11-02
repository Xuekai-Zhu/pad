def solution():
    """Sarah decided to pull weeds from her garden. On Tuesday she pulled 25 weeds. The next day she pulled three times the number of weeds she did the day before. On Thursday her allergies bothered her and she could only pull up one-fifth of the weeds she pulled on the day before. Finally, on Friday it rained for half the day and she managed to pull up 10 fewer weeds than she did on Thursday. In total, how many weeds did she pull up?"""
    # Define the number of weeds Sarah pulled on each day
    tuesday_weeds = 25
    wednesday_weeds = 3 * tuesday_weeds
    thursday_weeds = wednesday_weeds / 5
    friday_weeds = thursday_weeds - 10

    # Calculate the total number of weeds Sarah pulled
    total_weeds = tuesday_weeds + wednesday_weeds + thursday_weeds + friday_weeds

    # Display the total number of weeds Sarah pulled
    result = total_weeds
    return result

print(solution())