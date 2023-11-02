def solution():
    
    first_pair_price = 40
    second_pair_price = 60
    cheaper_pair_price = min(first_pair_price, second_pair_price)
    discounted_pair_price = cheaper_pair_price / 2
    total_price = first_pair_price + second_pair_price - cheaper_pair_price + discounted_pair_price
    total_price = total_price - (total_price * 0.25)
    result = total_price
    return result

print(solution())