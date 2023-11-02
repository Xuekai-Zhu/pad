def solution():
    """Mark wants to have a water balloon fight with his friends. He goes to the store to buy balloons and sees that they sell small bags for $4, medium bags for $6 and extra large bags for $12. He has $24 and wants to get the most balloons as possible. If the $4 bags contain 50 balloons, the $6 bags contain 75 balloons and the $12 bags contain 200 balloons, what is the greatest number of balloons he can buy?"""
    budget = 24
    
    # Calculate number of balloons per dollar for each bag size
    small = 50/4
    medium = 75/6
    large = 200/12
    
    # Find the maximum number of balloons he can buy
    max_balloons = 0
    for i in range(budget//4 + 1):
        for j in range(budget//6 + 1):
            for k in range(budget//12 + 1):
                total_balloons = i*small + j*medium + k*large
                total_cost = i*4 + j*6 + k*12
                if total_cost <= budget and total_balloons > max_balloons:
                    max_balloons = total_balloons
    
    result = max_balloons
    return result

print(solution())