def solution():
    # Calculate the number of marbles bought by Ludo and Michael
    ludo_marbles = 16 * (5/4) # Ludo bought 1/4 times more marbles than Wolfgang
    michael_marbles = 2/3 * (16 + ludo_marbles) # Michael bought 2/3 times as many marbles as the number of marbles both Wolfgang and Ludo bought
    
    # Calculate the total number of marbles
    total_marbles = 16 + ludo_marbles + michael_marbles
    
    # Calculate the number of marbles each friend gets if they divide them equally
    each_gets = total_marbles // 3
    
    result = each_gets
    return result

print(solution())