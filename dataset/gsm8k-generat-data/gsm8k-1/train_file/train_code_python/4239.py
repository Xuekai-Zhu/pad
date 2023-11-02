def solution():
    """When Diane turns 30, she will be half the age of Alex and twice as old as Allison. Diane is 16 years old now. What is the sum of the ages of Alex and Allison now?"""
    diane_now = 16
    diane_future = 30
    alex_future = diane_future * 2
    allison_future = diane_future / 2
    alex_now = alex_future - (diane_future - diane_now)
    allison_now = allison_future - (diane_future - diane_now)
    result = alex_now + allison_now
    return result

print(solution())