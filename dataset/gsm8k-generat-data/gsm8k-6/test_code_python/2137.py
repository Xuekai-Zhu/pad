def solution():
    # Calculate the total number of tomatoes after Grandpa came back from vacation
    total_tomatoes = 36 * 100  # Grandpa counted 100 times more tomatoes when he came back from vacation
    tomatoes_grew_in_absence = total_tomatoes - 36  # subtract the initial number of tomatoes to get the number that grew in Grandpa's absence
    result = tomatoes_grew_in_absence
    return result

print(solution())