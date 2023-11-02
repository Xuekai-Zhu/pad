def solution():
    yvonne_words = 400
    janna_words = yvonne_words + 150
    total_words = yvonne_words + janna_words

    # Calculate the net change in words after editing
    net_change = 2 * 20 - 20  # they added twice as many words as they removed, so the net change is 2*20 - 20

    # Calculate the number of words they still need to add to reach the 1000-word requirement
    remaining_words = 1000 - total_words + net_change

    result = remaining_words
    return result

print(solution())