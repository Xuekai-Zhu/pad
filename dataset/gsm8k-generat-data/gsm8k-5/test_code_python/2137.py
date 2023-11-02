def solution():
    # Grandpa had 36 small tomatoes before going on vacation
    initial_count = 36

    # Grandpa counted 100 times more tomatoes when he came back from vacation
    final_count = initial_count * 100

    # Calculate the number of tomatoes that grew in Grandpa's absence
    grew_count = final_count - initial_count

    result = grew_count
    return result

print(solution())