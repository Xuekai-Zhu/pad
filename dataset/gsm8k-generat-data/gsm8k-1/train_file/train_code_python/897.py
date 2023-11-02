def solution():
    """Tony wants to build the longest rope he possibly can, so he collects all the rope in his home. 
    He finds an 8-foot rope, a 20-foot rope, three 2 foot ropes, and a 7-foot rope. 
    Each knot between the ropes makes him lose 1.2 foot per knot. How long is his rope when he's done tying them all together?"""
    ropes = [8, 20, 2, 2, 2, 7]
    knots = len(ropes) - 1
    total_length = sum(ropes) - (knots * 1.2)
    result = total_length
    return result

print(solution())