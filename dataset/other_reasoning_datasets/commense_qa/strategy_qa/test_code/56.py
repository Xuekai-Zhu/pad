def solution():
    original_name = "ayokonetl"
    top_row_keys = "qwertyuiop"
    # Check if all letters in the original name can be found in the top row keys
    if all(letter in top_row_keys for letter in original_name):
        result = "yes"
    else:
        result = "no"
    return result

print(solution())