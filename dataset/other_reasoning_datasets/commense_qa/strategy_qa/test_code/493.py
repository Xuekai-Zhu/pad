def solution():
    declaration_languages = ["Albanian", "Gheg", "Tosk", "Ottoman Turkish"]
    arvanite_greek_language = "Tosk"
    if arvanite_greek_language in declaration_languages:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())