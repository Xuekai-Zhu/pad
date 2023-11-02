def solution():
    is_a_tale_of_two_cities_original = True
    is_the_bible_a_religious_text = True
    is_a_parody_of_the_bible = False
    if is_a_tale_of_two_cities_original and is_the_bible_a_religious_text and not is_a_parody_of_the_bible:
        result = "no"
    else:
        result = "yes"
    return result

print(solution())