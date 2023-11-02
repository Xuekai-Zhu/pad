def solution():
    """The middle school sold 6 more than two times the number of fair tickets as it did tickets to the baseball game. 
    If 25 fair tickets were sold, how many baseball game tickets did the school sell?"""
    fair_tickets_sold = 25
    baseball_tickets_sold = (fair_tickets_sold * 2) + 6
    result = baseball_tickets_sold
    return result

print(solution())