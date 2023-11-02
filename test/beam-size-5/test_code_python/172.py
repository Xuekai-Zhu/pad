def solution():
    num_asians = 240
    num_japanese = 80
    num_chinese = 60 - num_asians - num_japanese

    # Calculate the number of girls on the Chinese team
    num_girls = num_chinese - num_boys
    result = num_girls
    return result

print(solution())