def solution():
    haiku_length = 60
    tweet_length = 140
    if haiku_length <= tweet_length:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())