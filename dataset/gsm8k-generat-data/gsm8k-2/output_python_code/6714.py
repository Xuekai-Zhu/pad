def solution():
    """Christine and Janice are having a contest to see who can throw a ball the highest. They each get three throws. On her first throw, Christine throws it 20 feet high. Janice's throw is 4 feet lower than Christine's. On their second throw, Christine throws it ten feet higher than her first throw and Janice throws it twice as high as her first throw. On the final throw, Christine throws it 4 feet higher than her 2nd throw while Janice throws it 17 feet higher than Christine's first throw. What is the height of the highest throw?"""
    christine_throws = [20, 30, 34]
    janice_throws = [16, 40, 37]
    
    highest_throw = max(max(christine_throws), max(janice_throws))
    
    result = highest_throw
    return result

print(solution())