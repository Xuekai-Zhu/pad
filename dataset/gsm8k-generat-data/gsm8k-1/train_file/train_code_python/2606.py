def solution():
    """John's dog has a litter of 8 puppies. He gives away half of them. He keeps one of the remaining puppies. He then takes the remaining puppies and sells them each for $600. He had to give the owner of the stud $300. How much money does he profit?"""
    litter_size = 8
    given_away = litter_size / 2
    remaining = litter_size - given_away - 1
    sale_price = 600
    stud_fee = 300
    profit = (remaining * sale_price) - stud_fee
    result = profit
    return result

print(solution())