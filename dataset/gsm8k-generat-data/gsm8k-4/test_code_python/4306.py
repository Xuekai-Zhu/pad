def solution():
    """There are 920 deer in a park. 10% of the deer have 8 antlers, and a quarter of that number also have albino fur. How many albino 8-antlered deer are there?"""
    # Define the total number of deer in the park
    total_deer = 920

    # Calculate the number of deer with 8 antlers
    eight_antler_deer = total_deer * 0.1

    # Calculate the number of albino deer with 8 antlers
    albino_eight_antler_deer = eight_antler_deer * 0.25

    # Return the result
    result = albino_eight_antler_deer
    return result

print(solution())