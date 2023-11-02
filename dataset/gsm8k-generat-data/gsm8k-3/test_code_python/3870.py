def solution():
    """Alexander Bought 22 more joggers than Tyson. Christopher bought twenty times as many joggers as Tyson. If Christopher bought 80 joggers, how many more joggers does Christopher buy than Alexander?"""
    # Let x be the number of joggers Tyson bought
    # Alexander bought 22 more joggers than Tyson, so Alexander bought x + 22 joggers
    # Christopher bought twenty times as many joggers as Tyson, so Christopher bought 20x joggers

    # If Christopher bought 80 joggers, then 20x = 80, so x = 4
    x = 4

    # Alexander bought x + 22 = 4 + 22 = 26 joggers
    alexander_joggers = x + 22

    # Christopher bought 20x = 20 * 4 = 80 joggers
    christopher_joggers = 20 * x

    # Christopher bought how many more joggers than Alexander?
    more_joggers = christopher_joggers - alexander_joggers

    # Display the result
    result = more_joggers
    return result

print(solution())