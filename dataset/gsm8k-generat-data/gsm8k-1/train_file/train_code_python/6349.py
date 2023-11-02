def solution():
    """Jackson's mother made little pizza rolls for Jackson's birthday party. Jackson ate 10 pizza rolls and his friend Jerome ate twice that amount. Tyler at one and half times more than Jerome. How many more pizza rolls did Tyler eat than Jackson?"""
    jackson_eaten = 10
    jerome_eaten = 2 * jackson_eaten
    tyler_eaten = 1.5 * jerome_eaten
    difference = tyler_eaten - jackson_eaten
    result = difference
    return result

print(solution())