def solution():
    """At a recent fishing tournament, Alex caught 7 times as many fish as Jacob. Jacob did not think that he had any chance of winning, but Alex became overconfident and knocked over his bucket of fish, 
    losing 23 fish back to the lake. If Jacob had 8 fish at the beginning, how many more fish does he need to catch to beat Alex by just 1 fish?"""
    # Calculate how many fish Alex originally caught
    alex_original = 7 * 8

    # Calculate how many fish Alex had after losing 23
    alex_after_loss = alex_original - 23

    # Calculate the minimum number of fish Jacob needs to catch to beat Alex by one
    min_jacob_catch = alex_after_loss - 1 - 8

    # Display the minimum number of fish Jacob needs to catch
    result = min_jacob_catch
    return result

print(solution())