def solution():
    """There were 20 fishermen in the lake who had cast their net to catch fish. If they caught 10000 fish in total, and 19 of them caught 400 fish each with their own net, calculate the number of fish the twentieth fisherman caught."""
    # Define the total number of fish caught
    total_fish = 10000

    # Define the number of fishermen who caught 400 fish each
    n = 19
    fish_per_n = 400

    # Calculate the total number of fish caught by these fishermen
    fish_caught_n = n * fish_per_n

    # Calculate the number of fish caught by the twentieth fisherman
    fish_caught_20 = total_fish - fish_caught_n

    # Return the result
    result = fish_caught_20
    return result

print(solution())