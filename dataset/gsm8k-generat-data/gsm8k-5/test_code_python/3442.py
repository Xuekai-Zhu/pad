def solution():
    # Calculate the number of cakes Gary can make
    cakes = 4 / 0.5  # 4 pounds of flour can make 8 cakes

    # Calculate the number of cupcakes Gary can make
    cupcakes = 2 / (1/5)  # 2 pounds of flour can make 10 cupcakes

    # Calculate the total earnings from selling the cakes and cupcakes
    total_earnings = (cakes * 2.5) + (cupcakes * 1)

    result = total_earnings
    return result

print(solution())