def solution():
    
    total_bowls = 70
    bowls_given = 2 * (sum([20 for i in range(10)]) // 10)
    remaining_bowls = total_bowls - bowls_given
    result = remaining_bowls
    return result

print(solution())