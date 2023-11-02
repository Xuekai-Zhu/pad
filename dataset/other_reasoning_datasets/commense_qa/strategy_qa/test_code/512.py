def solution():
    poem_author = "Homer"
    baseball_term = "Home Run"
    if baseball_term.startswith("Homer") and poem_author.lower() in baseball_term.lower():
        result = "yes"
    else:
        result = "no"
    return result

print(solution())