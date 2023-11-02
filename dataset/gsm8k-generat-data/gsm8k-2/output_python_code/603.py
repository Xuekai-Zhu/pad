def solution():
    """Santana has 7 brothers. 3 of them have birthdays in March, 1 of them has a birthday in October, 1 has a birthday in November, and another 2 of them were born in December. If Santana always buys each of her brothers a birthday present and a Christmas present, how many more presents does she have to buy in the second half of the year than the first half of the year?"""
    first_half_brothers = 3
    second_half_brothers = 4
    first_half_presents = (first_half_brothers * 2) + 1
    second_half_presents = (second_half_brothers * 2) + 1
    diff_presents = second_half_presents - first_half_presents
    result = diff_presents
    return result

print(solution())