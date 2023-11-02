def solution():
    # Calculate the amount of cake Nathalie ate
    nathalie_cake = 400/8  # Each part is 1/8 of the cake

    # Calculate the amount of cake Pierre ate
    pierre_cake = 2 * nathalie_cake

    # Convert the amount of cake Pierre ate to grams
    pierre_grams = pierre_cake * 100  # 1/8 of the cake is 50 grams

    result = pierre_grams
    return result

print(solution())