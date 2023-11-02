def solution():
    """Dan can get to the center of a lollipop in 58 licks. Micheal does it in 63 licks. Sam & David each take 70 licks to get to the center of a lollipop while Lance only needs 39 licks. What is the average amount of licks it takes to get to the center of a lollipop?"""
    dan = 58
    michael = 63
    sam = 70
    david = 70
    lance = 39
    
    total_licks = dan + michael + sam + david + lance
    num_of_people = 5
    
    avg_licks = total_licks / num_of_people
    result = avg_licks
    
    return result

print(solution())