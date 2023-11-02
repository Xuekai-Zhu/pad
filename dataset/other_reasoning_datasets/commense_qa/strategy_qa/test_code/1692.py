def solution():
    coen_brothers_language = "English"
    guinea_bissau_languages = ["Creole", "Native African languages", "Portuguese"]
    if coen_brothers_language not in guinea_bissau_languages:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())