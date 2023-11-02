def solution():
    """Christine and Janice are having a contest to see who can throw a ball the highest.
    They each get three throws. On her first throw, Christine throws it 20 feet high.
    Janice's throw is 4 feet lower than Christine's.
    On their second throw, Christine throws it ten feet higher than her first throw and
    Janice throws it twice as high as her first throw.
    On the final throw, Christine throws it 4 feet higher than her 2nd throw while
    Janice throws it 17 feet higher than Christine's first throw.
    What is the height of the highest throw?"""
    
    christine_f1 = 20
    janice_f1 = christine_f1 - 4
    
    christine_f2 = christine_f1 + 10
    janice_f2 = janice_f1 * 2
    
    christine_f3 = christine_f2 + 4
    janice_f3 = christine_f1 + 17
    
    highest_throw = max(christine_f3, janice_f3)
    result = highest_throw
    return result

print(solution())