def solution():
    """Davonte is trying to figure out how much space his art collection takes up. He measures his paintings and finds he has three square 6-foot by 6-foot paintings, four small 2-foot by 3-foot paintings, and one large 10-foot by 15-foot painting. How many square feet does his collection take up?"""
    sq_ft_per_6x6 = 36*3
    sq_ft_per_2x3 = 2*3*4
    sq_ft_per_10x15 = 10*15
    total_sq_ft = sq_ft_per_6x6 + sq_ft_per_2x3 + sq_ft_per_10x15
    result = total_sq_ft
    return result

print(solution())