def solution():
    """Alexander Bought 22 more joggers than Tyson. Christopher bought twenty times as many joggers as Tyson. If Christopher bought 80 joggers, how many more joggers does Christopher buy than Alexander?"""
    christopher_joggers = 80
    tyson_joggers = christopher_joggers / 20
    alexander_joggers = tyson_joggers - 22
    joggers_difference = christopher_joggers - alexander_joggers
    result = joggers_difference
    return result

print(solution())