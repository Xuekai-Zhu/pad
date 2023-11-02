def solution():
    # Calculate the amount of data Elsa has left after using some for Youtube and Facebook
    remaining_data = 500 - 300  # 300 MB spent on Youtube
    remaining_data *= (3/5)  # 2/5 is spent on Facebook, so 3/5 is left
    result = remaining_data
    return result

print(solution())