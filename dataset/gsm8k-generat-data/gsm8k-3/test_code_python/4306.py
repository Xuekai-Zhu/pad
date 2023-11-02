def solution():
    """There are 920 deer in a park. 10% of the deer have 8 antlers, and a quarter of that number also have albino fur. How many albino 8-antlered deer are there?"""
    # Calculate the number of deer with 8 antlers
    deer_with_eight_antlers = 0.1 * 920

    # Calculate the number of deer with both 8 antlers and albino fur
    albino_eight_antlered_deer = 0.25 * deer_with_eight_antlers

    # Display the number of albino 8-antlered deer
    result = albino_eight_antlered_deer
    return result

print(solution())