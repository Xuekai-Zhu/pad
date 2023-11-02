def solution():
    women_preceding_john_key = 2
    women_succeeding_john_key = 1
    if women_succeeding_john_key > women_preceding_john_key:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())