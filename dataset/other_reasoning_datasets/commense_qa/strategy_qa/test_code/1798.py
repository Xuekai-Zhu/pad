def solution():
    san_antonio = "city in Texas"
    boris_johnson = "Prime Minister of the UK"
    uk_citizens_only = True
    if san_antonio != "in the UK" and not uk_citizens_only:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())