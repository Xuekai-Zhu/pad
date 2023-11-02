def solution():
    """One hundred chips were divided by Ian and Lyle in the ratio 4:6. What percentage of the chips did Lyle have?"""
    # Find the total number of parts in the ratio
    total_parts = 4 + 6

    # Find the number of parts that Lyle received
    lyle_parts = 6

    # Calculate the percentage of chips that Lyle received
    lyle_percentage = (lyle_parts / total_parts) * 100

    # Display the percentage of chips that Lyle received
    result = lyle_percentage
    return result

print(solution())