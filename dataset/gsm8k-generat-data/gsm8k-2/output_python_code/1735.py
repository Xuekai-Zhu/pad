def solution():
    """A box of chocolate bars was shared equally between Mike, Rita and Anita. If the box contains 12 bars, how many bars did Mike and Rita get (combined)?"""
    total_bars = 12
    mike_and_rita_bars = total_bars // 3 * 2
    result = mike_and_rita_bars
    return result

print(solution())