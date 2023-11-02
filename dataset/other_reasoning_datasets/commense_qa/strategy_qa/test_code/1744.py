def solution():
    # Define the fact that black swans fly in a V formation and the longest word in the dictionary
    black_swan_formation = "V"
    longest_word = "pneumonoultramicroscopicsilicovolcanoconiosis"
    # Check if the formation type can help spell the longest word
    if black_swan_formation in longest_word:
        result = "yes"
    else:
        result = "no"
    return result

print(solution())