def solution():
    """A box of chocolate bars was shared equally between Mike, Rita and Anita. If the box contains 12 bars, how many bars did Mike and Rita get (combined)?"""
    # Calculate the number of bars each person gets
    per_person = 12 // 3

    # Calculate the number of bars Mike and Rita get combined
    mike_and_rita = per_person * 2

    # Display the number of bars Mike and Rita get combined
    result = mike_and_rita
    return result

print(solution())