def solution():
    #Define initial savings amount and savings pattern as a list
    savings = 2
    savings_pattern = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]

    #Loop through savings_pattern list to calculate total savings by December
    for i in range(1, 12):
        savings += savings_pattern[i]

    result = savings
    return result

print(solution())