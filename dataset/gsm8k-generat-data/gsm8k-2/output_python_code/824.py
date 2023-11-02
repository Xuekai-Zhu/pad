def solution():
    """James decides to buy a new bed and bed frame. The bed frame is $75 and the bed is 10 times that price. He gets a deal for 20% off. How much does he pay for everything?"""
    bed_frame_price = 75
    bed_price = 10 * bed_frame_price
    total_price = bed_frame_price + bed_price
    discount = 0.2 * total_price
    final_price = total_price - discount
    result = final_price
    return result

print(solution())