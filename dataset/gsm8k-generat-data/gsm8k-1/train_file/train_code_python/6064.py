def solution():
    """Anna has 50 pencils and Harry has twice the number of Anna’s pencils but he lost 19 of them. How many pencils are left with Harry?"""
    anna_pencils = 50
    harry_pencils = anna_pencils * 2
    harry_pencils -= 19
    result = harry_pencils
    return result

print(solution())