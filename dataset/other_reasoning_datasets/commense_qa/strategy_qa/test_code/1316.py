def solution():
    nb_official_languages = ["French", "English"]
    burundi_official_languages = ["French"]
    common_language = [language for language in nb_official_languages if language in burundi_official_languages]
    if common_language:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())