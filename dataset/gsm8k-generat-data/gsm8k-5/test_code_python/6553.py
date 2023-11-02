def solution():
    bananas_per_loaf = 4  # Elois needs 4 bananas to make 1 loaf of banana bread
    monday_loaves = 3  # Elois makes 3 loaves of banana bread on Monday
    tuesday_loaves = 2 * monday_loaves  # Elois makes twice as many loaves on Tuesday as Monday

    # Calculate the total number of loaves Elois makes
    total_loaves = monday_loaves + tuesday_loaves

    # Calculate the total number of bananas Elois uses to make all the banana bread
    total_bananas = total_loaves * bananas_per_loaf
    result = total_bananas
    return result

print(solution())