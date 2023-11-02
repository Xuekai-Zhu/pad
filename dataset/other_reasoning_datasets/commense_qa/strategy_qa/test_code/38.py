def solution():
    is_rabbi = True
    practices_judaism = True
    has_saints_and_martyrs = False
    killed_christians = True
    if is_rabbi and practices_judaism and not has_saints_and_martyrs and not killed_christians:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())