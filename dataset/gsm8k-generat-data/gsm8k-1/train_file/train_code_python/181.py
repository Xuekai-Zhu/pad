def solution():
    """Lisa and Carly go shopping together. Lisa spends $40 on t-shirts then spends half of this amount on jeans and twice this amount on coats. Carly spends only a quarter as much as Lisa on t-shirts but spends 3 times as much on jeans and a quarter of the amount Lisa spent on coats.
    In dollars, how much did Lisa and Carly spend in total?"""
    lisa_shirt_cost = 40
    lisa_jean_cost = lisa_shirt_cost / 2
    lisa_coat_cost = lisa_shirt_cost * 2
    carly_shirt_cost = lisa_shirt_cost / 4
    carly_jean_cost = lisa_jean_cost * 3
    carly_coat_cost = lisa_coat_cost / 4

    total_cost = lisa_shirt_cost + lisa_jean_cost + lisa_coat_cost + carly_shirt_cost + carly_jean_cost + carly_coat_cost
    result = total_cost

    return result

print(solution())