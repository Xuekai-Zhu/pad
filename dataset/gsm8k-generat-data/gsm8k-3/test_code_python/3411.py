def solution():
    """Lara is a contestant on a fun game show where she needs to navigate an inflated bouncy house obstacle course. First she needs to carry a backpack full of treasure through the obstacle course and set it down on the other side, which she does in 7 minutes and 23 seconds. Second, she needs to crank open the door to the obstacle course so she can go back through, which takes her 73 seconds. After she gets through the door she traverses the obstacle course again and makes it out faster without the backpack, in 5 minutes and 58 seconds. How many seconds total does it take her to complete the obstacle course?"""

    # Calculate the total time to complete the obstacle course
    total_time = (7 * 60 + 23) + 73 + (5 * 60 + 58)

    # Return the total time in seconds
    result = total_time
    return result

print(solution())