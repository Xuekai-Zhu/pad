def solution():
    """Christine and Janice are having a contest to see who can throw a ball the highest. They each get three throws. On her first throw, Christine throws it 20 feet high. Janice's throw is 4 feet lower than Christine's. On their second throw, Christine throws it ten feet higher than her first throw and Janice throws it twice as high as her first throw. On the final throw, Christine throws it 4 feet higher than her 2nd throw while Janice throws it 17 feet higher than Christine's first throw. What is the height of the highest throw?"""
    # Define Christine's throws
    c_throw1 = 20
    c_throw2 = c_throw1 + 10
    c_throw3 = c_throw2 + 4

    # Define Janice's throws
    j_throw1 = c_throw1 - 4
    j_throw2 = 2 * j_throw1
    j_throw3 = c_throw1 + 17

    # Find the highest throw
    highest_throw = max(c_throw1, c_throw2, c_throw3, j_throw1, j_throw2, j_throw3)

    result = highest_throw
    return result

print(solution())