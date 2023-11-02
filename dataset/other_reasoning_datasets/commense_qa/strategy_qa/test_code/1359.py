def solution():
    # Define the characteristics of the Inuktitut language
    oral_language = True
    no_Latin_letters = True
    # Check if the letter B is present in the language
    if not oral_language and not no_Latin_letters:
        result = "possible"
    else:
        result = "unlikely"
    return result

print(solution())