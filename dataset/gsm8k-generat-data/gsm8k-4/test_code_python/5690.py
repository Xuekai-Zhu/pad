def solution():
    """Fred has 12 identical candy bars, and Uncle Bob has 6 more. If Jacqueline has ten times the total number of candy bars Fred and Uncle Bob have, what's 40% of Jacqueline's candy bars?"""
    # Define the initial number of candy bars
    fred_bars = 12
    bob_bars = fred_bars + 6
    total_bars = fred_bars + bob_bars

    # Calculate the number of candy bars Jacqueline has
    jacqueline_bars = total_bars * 10

    # Calculate 40% of Jacqueline's candy bars
    forty_percent_bars = jacqueline_bars * 0.4

    # return the result
    result = forty_percent_bars
    return result

print(solution())