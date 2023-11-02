def solution():
    """Grant has worked as a freelance math worker for the last three months. The first month he made 350$. The second month he made 50$ more than double he made the first month. The third month he quadrupled the sum of the first two months. How much did Grant make in his first three months total?"""
    first_month = 350
    second_month = (2 * first_month) + 50
    third_month = 4 * (first_month + second_month)
    total = first_month + second_month + third_month
    result = total
    return result

print(solution())