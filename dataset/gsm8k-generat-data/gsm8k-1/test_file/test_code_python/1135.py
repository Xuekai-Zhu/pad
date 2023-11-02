def solution():
    """Russell orders his favorite bagels online. Each pack of bagels costs $10.00 and has 9 bagels in the pack. If he orders 4 packs of bagels, he will receive a 10% discount. After ordering 4 bags, how much will each single bagel cost?"""
    price_per_pack = 10
    bagels_per_pack = 9
    num_packs = 4
    discount_rate = 0.1
    total_price = (price_per_pack * num_packs) * (1 - discount_rate)
    total_bagels = bagels_per_pack * num_packs
    price_per_bagel = total_price / total_bagels
    result = price_per_bagel
    return result

print(solution())