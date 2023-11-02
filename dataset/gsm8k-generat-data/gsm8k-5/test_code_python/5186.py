def solution():
    # Determine James' current age
    james_future_age = 37
    james_current_age = james_future_age - 15

    # Determine Janet's current age
    janet_current_age = (james_current_age - 8) / 2

    # Determine Susan's current age
    susan_current_age = janet_current_age - 3

    # Determine Susan's age in 5 years
    susan_future_age = susan_current_age + 5
    result = susan_future_age
    return result

print(solution())