def solution():
    """Lisa and Carly go shopping together. Lisa spends $40 on t-shirts then spends half of this amount on jeans and twice this amount on coats. Carly spends only a quarter as much as Lisa on t-shirts but spends 3 times as much on jeans and a quarter of the amount Lisa spent on coats. In dollars, how much did Lisa and Carly spend in total?"""
    # Calculate Lisa's spending on jeans and coats
    lisa_tshirts = 40
    lisa_jeans = lisa_tshirts / 2
    lisa_coats = lisa_tshirts * 2
    lisa_total = lisa_tshirts + lisa_jeans + lisa_coats

    # Calculate Carly's spending on jeans and coats
    carly_tshirts = lisa_tshirts / 4
    carly_jeans = lisa_jeans * 3
    carly_coats = lisa_coats / 4
    carly_total = carly_tshirts + carly_jeans + carly_coats

    # Calculate the total spending of Lisa and Carly
    total_spending = lisa_total + carly_total

    # Return the result
    result = total_spending
    return result

print(solution())