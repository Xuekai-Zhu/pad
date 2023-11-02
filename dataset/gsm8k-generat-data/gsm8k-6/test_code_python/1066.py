def solution():
    # Calculate the total number of oranges and apples picked by George and Amelia
    oranges_george = 45
    apples_george = oranges_george + 5
    oranges_amelia = oranges_george - 18
    apples_amelia = 15
    total_fruits = oranges_george + apples_george + oranges_amelia + apples_amelia
    result = total_fruits
    return result

print(solution())