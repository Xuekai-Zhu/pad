def solution():
    """Before James starts the strength phase training of his cycle he has a powerlifting total of 2200 pounds at a bodyweight of 245 pounds.  He manages to gain 15% on his total and 8 pounds of body weight.  What is the ratio of his lifting total to bodyweight?"""
    
    # Define the initial powerlifting total and bodyweight
    initial_total = 2200
    initial_bodyweight = 245

    # Calculate the new powerlifting total and bodyweight after gaining
    new_total = initial_total * 1.15
    new_bodyweight = initial_bodyweight + 8

    # Calculate the ratio of the new powerlifting total to bodyweight
    ratio = new_total / new_bodyweight

    result = round(ratio, 2)
    return result

print(solution())