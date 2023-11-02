def solution():
    """The total number of whales in the sea this year is double what it was last year. If the World Animals Organization predicts that there will be 800 more whales in the sea next year, and the number of whales in the sea last year was 4000, calculate the total number of whales in the sea next year if the predictions are accurate."""
    # Calculate the number of whales in the sea this year
    whales_this_year = 2 * 4000

    # Calculate the number of whales in the sea next year
    whales_next_year = whales_this_year + 800

    # Display the total number of whales in the sea next year
    result = whales_next_year
    return result

print(solution())