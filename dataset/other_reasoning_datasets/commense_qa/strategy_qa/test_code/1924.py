def solution():
    # Define Woodrow Wilson's support for the Ku Klux Klan and the Klan's belief about Blacks
    wilson_supports_kkk = True
    kkk_believes_blacks_are_inferior = True
    # Check if Wilson believed Blacks to be equal members of society
    if not (wilson_supports_kkk and kkk_believes_blacks_are_inferior):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())