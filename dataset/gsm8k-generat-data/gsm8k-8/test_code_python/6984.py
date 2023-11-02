def solution():
    total_words = 1000
    yvonne_words = 400
    janna_words = yvonne_words + 150
    initial_total = yvonne_words + janna_words
    edited_total = initial_total - 20 + 2 * 20
    remaining_words = total_words - edited_total
    result = remaining_words
    return result

print(solution())