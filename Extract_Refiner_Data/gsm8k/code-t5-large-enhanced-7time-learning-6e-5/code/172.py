def solution():
    
    # Define the total number of Asians and the number of Japanese
    total_asians = 240
    japanese_asians = 80

    # Calculate the number of Chinese asians
    chinese_asians = total_asians - japanese_asians

    # Calculate the number of girls on the Chinese team
    girls = chinese_asians - 60

    # return the result
    result = girls
    return result

print(solution())