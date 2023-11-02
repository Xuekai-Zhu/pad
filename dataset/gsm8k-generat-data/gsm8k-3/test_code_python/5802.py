def solution():
    """Hannah ran 9 kilometers on Monday. She ran 4816 meters on Wednesday and 2095 meters on Friday. How many meters farther did she run on Monday than Wednesday and Friday combined?"""
    # Convert Monday's distance to meters
    monday_distance = 9 * 1000

    # Calculate Wednesday and Friday's combined distance
    wed_fri_distance = 4816 + 2095

    # Calculate the difference between Monday's distance and Wednesday and Friday's combined distance
    diff = monday_distance - wed_fri_distance

    # Display the result
    result = diff
    return result

print(solution())