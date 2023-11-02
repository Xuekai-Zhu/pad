def solution():
    """Brendan can cut 8 yards of grass per day, he bought a lawnmower and it helped him to cut more yards by Fifty percent per day. How many yards will Brendan be able to cut after a week?"""
    initial_cut = 8
    increased_cut = initial_cut * 1.5
    total_after_week = (initial_cut*7) + (increased_cut*7)
    result = total_after_week
    return result

print(solution())