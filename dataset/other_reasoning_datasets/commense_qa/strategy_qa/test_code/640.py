def solution():
    # Define the two most common words in the English language
    common_words = ["the", "be"]
    # Check if the letter C is crucial to spelling either word
    if "c" in common_words[0] or "c" in common_words[1]:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())