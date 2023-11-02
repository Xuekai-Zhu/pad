def solution():
    # Let's assume Mark had x amount of money initially
    # Mark spends half of his money in the first store, so he has x/2 left
    # He then spends $14 more, leaving him with x/2 - 14
    # Mark spends one-third of his starting money in the second store, so he has 2/3*x left
    # He then spends $16 more, leaving him with 2/3*x - 16
    # We know that Mark has no money left, so we can set these two expressions equal to each other and solve for x:

    x/2 - 14 = 2/3*x - 16
    x/6 = 2
    x = 12

    # Therefore, Mark had $12 when he entered the first store
    result = 12
    return result

print(solution())