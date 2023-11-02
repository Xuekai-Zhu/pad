def solution():
    """$18 is shared among 3 boys. The eldest added $5 to his share and added another $10 the following day. He later needed some money and spent $8 from his total so far. After saving some more, he was able to triple the amount he had left after spending the $8. How much does he have now?"""
    total_money = 18
    num_boys = 3
    youngest_share = total_money / num_boys
    eldest_share = youngest_share + 5
    eldest_share += 10
    eldest_share -= 8
    remaining_money = eldest_share
    remaining_money *= 3
    result = remaining_money
    
    return result

print(solution())