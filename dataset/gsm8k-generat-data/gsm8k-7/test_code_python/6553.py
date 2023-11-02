def solution():
    bananas_per_loaf = 4
    monday_loaves = 3
    tuesday_loaves = monday_loaves * 2

    # Calculate the total number of loaves Elois made
    total_loaves = monday_loaves + tuesday_loaves

    # Calculate the total number of bananas Elois used
    total_bananas = total_loaves * bananas_per_loaf
    result = total_bananas
    return result

print(solution())