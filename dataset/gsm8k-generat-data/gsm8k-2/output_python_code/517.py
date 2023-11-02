def solution():
    """Merill has twice as many marbles as Elliot and the two of them together have five fewer marbles than Selma. If Selma has fifty marbles, how many marbles does Merill have?"""
    selma_marbles = 50
    total_marbles = selma_marbles - 5
    elliot_marbles = (total_marbles - merill_marbles) / 3
    merill_marbles = elliot_marbles * 2
    result = merill_marbles
    return result

print(solution())