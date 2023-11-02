def solution():
    tyson_joggers = 80 / 20  # Christopher bought 20 times as many joggers as Tyson, so Tyson bought 1/20th of what Christopher bought
    alexander_joggers = tyson_joggers - 22  # Alexander bought 22 more joggers than Tyson
    christopher_alexander_diff = 80 - (alexander_joggers + 22)  # Find the difference between the number of joggers Christopher and Alexander bought
    result = christopher_alexander_diff
    return result

print(solution())