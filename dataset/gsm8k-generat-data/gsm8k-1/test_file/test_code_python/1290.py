def solution():
    """Jake is shopping at a clothing store. The store has a buy one get one 50% off deal on T-shirts. Jake buys 2 T-shirts. The original price of each T-shirt is $8. Then, Jake buys a pair of shoes that is 40% off the original price. The original price of the shoes is $40. What is the total amount of money Jake spends at the store?"""
    tshirt_price = 8
    tshirt_discount = 0.5
    num_tshirts = 2
    shoe_price = 40
    shoe_discount = 0.4

    tshirt_total = num_tshirts * tshirt_price - (num_tshirts // 2) * (tshirt_price * tshirt_discount)
    shoe_total = shoe_price * (1 - shoe_discount)
    total_spent = tshirt_total + shoe_total

    return total_spent

print(solution())