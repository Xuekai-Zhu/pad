def solution():
    """Lizzie has half as many crayons as Bobbie. Bobbie has three times as many crayons as Billie. If Billie has 18 crayons, how many crayons does Lizzie have?"""
    billie_crayons = 18
    bobbie_crayons = billie_crayons * 3
    lizzie_crayons = bobbie_crayons / 2
    result = lizzie_crayons
    return result

print(solution())