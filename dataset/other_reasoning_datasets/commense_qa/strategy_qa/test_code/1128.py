def solution():
    spoken_languages = ["Cantonese", "Mandarin", "English"]
    sign_languages = ["American Sign Language"]
    overlap = [language for language in spoken_languages if language in sign_languages]
    if overlap:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())