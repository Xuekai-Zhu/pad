def solution():
    """Brendan went fishing with his dad. Brenden caught 8 fish in the morning. He threw 3 back that were too small. He caught 5 more in the afternoon. Brendan’s dad caught 13 fish. How many fish did they catch in all?"""
    # Calculate the total number of fish Brendan caught
    brendan_total = 8 - 3 + 5

    # Calculate the total number of fish they caught together
    total_catch = brendan_total + 13

    # Display the total catch
    result = total_catch
    return result

print(solution())