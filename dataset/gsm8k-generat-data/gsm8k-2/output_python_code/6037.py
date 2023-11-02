def solution():
    """Mary has 3 times as much candy as Megan. Mary then adds 10 more pieces of candy to her collection. If Megan has 5 pieces of candy, how many does Mary have in total?"""
    megan_candy = 5
    mary_candy = 3 * megan_candy + 10
    total_candy = megan_candy + mary_candy
    result = total_candy
    return result

print(solution())