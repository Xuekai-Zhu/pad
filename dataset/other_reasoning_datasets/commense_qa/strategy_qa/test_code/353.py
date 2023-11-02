def solution():
    owners = ["Warner Bros.", "Turner Entertainment"]
    characters = ["Tom and Jerry"]
    disney_characters = ["Disney characters"]
    if any(owner in owners for owner in disney_characters) and any(character in characters for character in disney_characters):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())