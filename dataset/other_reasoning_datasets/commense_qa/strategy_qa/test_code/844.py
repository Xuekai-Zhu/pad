def solution():
    novel_subject = "Three Kingdoms Period"
    emperor_ancestors = "not mentioned"
    if novel_subject not in emperor_ancestors:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())