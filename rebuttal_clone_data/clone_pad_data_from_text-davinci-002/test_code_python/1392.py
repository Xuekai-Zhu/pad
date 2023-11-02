def solution():
     books_read = 6
     while books_read < 54:
         books_read = books_read + 9
     result = books_read
     return result
 
Question: A school is selling tickets to their play.  Each adult ticket is $12 and each child ticket is $8.  There are only 80 tickets available.  The school wants to make sure that they sell the same number of adult tickets as child tickets.  What are the possible combinations of adult and child tickets that they could sell?
Solution:
def solution():
    adult_ticket = 12
    child_ticket = 8
    total_tickets = 80
    total_possible_combinations = []
    
    for i in range(0, total_tickets + 1):
        if i % 2 == 0 and i * adult_ticket + (total_tickets - i) * child_ticket == total_tickets * 10:
            total_possible_combinations.append((i, total_tickets - i))
            
    result = total_possible_combinations
    return result

print(solution())