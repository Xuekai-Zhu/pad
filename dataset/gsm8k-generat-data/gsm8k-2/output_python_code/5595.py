def solution():
    """The total number of whales in the sea this year is double what it was last year. If the World Animals Organization predicts that there will be 800 more whales in the sea next year, and the number of whales in the sea last year was 4000, calculate the total number of whales in the sea next year if the predictions are accurate."""
    last_year = 4000
    this_year = last_year * 2
    next_year = this_year + 800
    result = next_year
    return result

print(solution())