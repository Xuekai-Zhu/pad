def solution():
    litter_size = 8
    puppies_kept = 1
    puppies_sold = litter_size - puppies_kept - (litter_size / 2)
    price_per_puppy = 600
    stud_fee = 300
    total_profit = (puppies_sold * price_per_puppy) - stud_fee
    result = total_profit
    return result

print(solution())