def solution():
    """Santana has 7 brothers. 3 of them have birthdays in March, 1 of them has a birthday in October, 1 has a birthday in November, and another 2 of them were born in December. If Santana always buys each of her brothers a birthday present and a Christmas present, how many more presents does she have to buy in the second half of the year than the first half of the year?"""
    first_half_presents = 7 * 2
    march_bdays = 3
    oct_bdays = 1
    nov_bdays = 1
    dec_bdays = 2
    second_half_presents = (march_bdays + oct_bdays + nov_bdays + dec_bdays) * 2
    result = second_half_presents - first_half_presents
    return result

print(solution())