def solution():
    """Michael and Thomas are selling their lego collections. They agree to split any money they earn. They sell them based on how many circles are on top. Each circle costs 1 cent. They earned $5 each after selling 100 single pieces, 45 double pieces, 50 triple pieces and a number of quadruple pieces. How many quadruple pieces did they sell?"""
    # Calculate the total amount earned from selling single, double, and triple circle pieces
    tot_earned = 5 * 2
    tot_earned -= 100 # account for cost of single circle pieces
    tot_earned -= 45 * 2 # account for cost of double circle pieces
    tot_earned -= 50 * 3 # account for cost of triple circle pieces

    # Calculate the number of quadruple circle pieces sold
    num_quadruples = tot_earned // 4

    # Display the number of quadruple circle pieces sold
    result = num_quadruples
    return result

print(solution())