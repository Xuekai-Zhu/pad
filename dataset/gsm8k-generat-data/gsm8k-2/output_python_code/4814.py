def solution():
    """Zayne sells bracelets for $5 each and two for $8. If he started with 30 bracelets and made $60 from selling bracelets for $5 each, how much in total did he make from selling his bracelets?"""
    starting_bracelets = 30
    price_each = 5
    price_two = 8
    sold_price_each = 60
    sold_count_each = sold_price_each // price_each
    sold_count_two = (starting_bracelets - sold_count_each) // 2
    total_sold_count = sold_count_each + (2 * sold_count_two)
    total_money = (sold_count_each * price_each) + (sold_count_two * price_two)
    result = total_money
    return result

print(solution())