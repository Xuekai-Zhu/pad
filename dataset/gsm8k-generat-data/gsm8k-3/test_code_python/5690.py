def solution():
    """Fred has 12 identical candy bars, and Uncle Bob has 6 more. If Jacqueline has ten times the total number of candy bars Fred and Uncle Bob have, what's 40% of Jacqueline's candy bars?"""
    # Calculate the total number of candy bars Fred and Uncle Bob have
    total_candy_bars = 12 + (12 + 6)

    # Calculate the number of candy bars Jacqueline has
    jacqueline_candy_bars = total_candy_bars * 10

    # Calculate 40% of Jacqueline's candy bars
    forty_percent = jacqueline_candy_bars * 0.4

    # Display the result
    result = forty_percent
    return result

print(solution())