def solution():
    """The total number of whales in the sea this year is double what it was last year. If the World Animals Organization predicts that there will be 800 more whales in the sea next year, and the number of whales in the sea last year was 4000, calculate the total number of whales in the sea next year if the predictions are accurate."""
    # Define the number of whales in the sea last year
    whales_last_year = 4000

    # Calculate the number of whales in the sea this year, which is double the number last year
    whales_this_year = whales_last_year * 2

    # Calculate the predicted number of whales in the sea next year, which is the number this year plus 800
    whales_next_year = whales_this_year + 800

    # return the result
    result = whales_next_year
    return result

print(solution())