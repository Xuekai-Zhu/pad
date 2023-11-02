def solution():
    # Find the number of joggers Tyson bought
    tyson_joggers = (80 / 20)  # Christopher bought twenty times as many joggers as Tyson

    # Find the number of joggers Alexander bought
    alexander_joggers = tyson_joggers - 22  # Alexander bought 22 more joggers than Tyson

    # Find the difference in joggers between Christopher and Alexander
    diff_joggers = 80 - alexander_joggers

    result = diff_joggers
    return result

print(solution())