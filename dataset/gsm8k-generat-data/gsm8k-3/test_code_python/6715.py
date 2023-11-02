def solution():
    """Christine and Janice are having a contest to see who can throw a ball the highest. They each get three throws. On her first throw, Christine throws it 20 feet high. Janice's throw is 4 feet lower than Christine's. On their second throw, Christine throws it ten feet higher than her first throw and Janice throws it twice as high as her first throw. On the final throw, Christine throws it 4 feet higher than her 2nd throw while Janice throws it 17 feet higher than Christine's first throw. What is the height of the highest throw?"""
    # Define Christine's first throw height
    christine_1 = 20

    # Define Janice's first throw height
    janice_1 = christine_1 - 4

    # Define Christine's second throw height
    christine_2 = christine_1 + 10

    # Define Janice's second throw height
    janice_2 = janice_1 * 2

    # Define Christine's third throw height
    christine_3 = christine_2 + 4

    # Define Janice's third throw height
    janice_3 = christine_1 + 17

    # Find the highest throw height
    highest_throw = max(christine_1, janice_1, christine_2,
                        janice_2, christine_3, janice_3)

    # Display the highest throw height
    result = highest_throw
    return result

print(solution())