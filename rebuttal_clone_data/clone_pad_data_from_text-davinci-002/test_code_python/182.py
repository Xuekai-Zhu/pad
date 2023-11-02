def solution():
    """Lisa and Carly go shopping together. Lisa spends $40 on t-shirts then spends half of this amount on jeans and twice this amount on coats. Carly spends only a quarter as much as Lisa on t-shirts but spends 3 times as much on jeans and a quarter of the amount Lisa spent on coats. In dollars, how much did Lisa and Carly spend in total?"""
    Lisa_total = 40 + (40 / 2) + (40 * 2)
    Carly_total = (40 / 4) + ((40 / 2) * 3) + (40 / 4)
    total_spent = Lisa_total + Carly_total
    result = total_spent
    return result

print(solution())