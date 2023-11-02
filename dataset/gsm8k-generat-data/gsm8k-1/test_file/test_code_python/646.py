def solution():
    """Samantha's last name has three fewer letters than Bobbie's last name. If Bobbie took two letters off her last name, she would have a last name twice the length of Jamie's. Jamie's full name is Jamie Grey. How many letters are in Samantha's last name?"""
    jamie_name_length = len("Grey")
    # Bobbie's last name is twice the length of Jamie's when two letters are removed
    bobbie_name_length = jamie_name_length * 2 + 2
    # Samantha's last name has three fewer letters than Bobbie's last name
    samantha_name_length = bobbie_name_length - 3
    result = samantha_name_length
    return result


def solution():
    """On Tuesday, Clara bought 20 pomegranates at $20 each. At the till she got $2 off because she had a voucher. The next day, the price shot to $30 per fruit, but the store also offered a 10% discount on the total cost. Sheila took advantage of the discount and bought 20 pomegranates. What is the difference between the final prices paid for the pomegranates on the two days?"""
    tuesday_price = 20
    tuesday_quantity = 20
    tuesday_voucher = 2
    tuesday_total = (tuesday_price * tuesday_quantity) - tuesday_voucher
    
    wednesday_price = 30
    wednesday_quantity = 20
    wednesday_discount_percent = 10
    wednesday_total = (wednesday_price * wednesday_quantity) * (1 - wednesday_discount_percent/100)
    
    difference = wednesday_total - tuesday_total
    result = difference
    return result

print(solution())