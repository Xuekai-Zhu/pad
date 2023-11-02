def solution():
    society_roles = ["promoting science and its benefits", "recognizing excellence in science",
                      "supporting outstanding science", "providing scientific advice for policy"]
    numerology_is_pseudoscience = True
    if "promoting science and its benefits" in society_roles and "recognizing excellence in science" in society_roles and not numerology_is_pseudoscience:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())