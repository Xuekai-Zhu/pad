def solution():
    """Ann, Bill, Cate, and Dale each buy personal pan pizzas cut into 4 pieces. If Bill and Dale eat 50% of their pizzas and Ann and Cate eat 75% of the pizzas, how many pizza pieces are left uneaten?"""
    total_pizzas = 4 * 4  # 16 pizza pieces
    bill_pizzas = 4 * 0.5  # 2 pizzas
    dale_pizzas = 4 * 0.5  # 2 pizzas
    ann_pizzas = 4 * 0.75  # 3 pizzas
    cate_pizzas = 4 * 0.75  # 3 pizzas
    total_eaten = bill_pizzas + dale_pizzas + ann_pizzas + cate_pizzas
    uneaten_pizzas = total_pizzas - total_eaten
    result = uneaten_pizzas
    return result

print(solution())