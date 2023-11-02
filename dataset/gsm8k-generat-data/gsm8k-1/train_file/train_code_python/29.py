def solution():
    """Ann, Bill, Cate, and Dale each buy personal pan pizzas cut into 4 pieces. If Bill and Dale eat 50% of their pizzas and Ann and Cate eat 75% of the pizzas, how many pizza pieces are left uneaten?"""
    total_pizzas = 4 * 4  # each person buys 4 slices of pizza
    bill_and_dale_pizzas = 2 * 4 * 0.5  # 2 people eat 50% of their pizzas
    ann_and_cate_pizzas = 2 * 4 * 0.75  # 2 people eat 75% of their pizzas
    total_pizzas_eaten = bill_and_dale_pizzas + ann_and_cate_pizzas 
    uneaten_pizzas = total_pizzas - total_pizzas_eaten
    uneaten_pieces = uneaten_pizzas * 4
    result = uneaten_pieces
    return result

print(solution())