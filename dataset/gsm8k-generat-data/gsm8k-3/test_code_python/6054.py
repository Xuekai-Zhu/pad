def solution():
    """There were 20 fishermen in the lake who had cast their net to catch fish. If they caught 10000 fish in total, and 19 of them caught 400 fish each with their own net, calculate the number of fish the twentieth fisherman caught."""
    # Calculate the total number of fish caught by the 19 fishermen
    fish_caught_19 = 19 * 400

    # Calculate the number of fish caught by the twentieth fisherman
    fish_caught_20 = 10000 - fish_caught_19

    # Display the number of fish caught by the twentieth fisherman
    result = fish_caught_20
    return result

print(solution())