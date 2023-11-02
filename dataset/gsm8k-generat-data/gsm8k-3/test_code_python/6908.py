def solution():
    """Before James starts the strength phase training of his cycle he has a powerlifting total of 2200 pounds at a bodyweight of 245 pounds.  He manages to gain 15% on his total and 8 pounds of body weight.  What is the ratio of his lifting total to bodyweight?"""
    # Define James' initial lifting total and body weight
    initial_total = 2200
    initial_weight = 245

    # Calculate James' new lifting total and body weight after gaining
    # 15% on his total and 8 pounds of body weight
    new_total = initial_total * 1.15
    new_weight = initial_weight + 8

    # Calculate the ratio of James' lifting total to body weight
    ratio = new_total / new_weight

    # Display the result
    result = ratio
    return result

print(solution())