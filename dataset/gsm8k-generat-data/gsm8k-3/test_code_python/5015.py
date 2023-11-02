def solution():
    """Jack cycles from his home to the store. Then he cycles, at the same speed, 50 miles to his friend Peter. It takes Jack twice as long to go from his home to the store as it takes to go from the store to his friend. If Peter and Jack now cycle back to the store together, how many miles in total have they cycled today?"""
    # Let's say Jack's speed is x
    # Distance from home to store = d1
    # Distance from store to Peter = d2

    # According to the problem, time taken for d1 is twice the time taken for d2
    # Hence, we can say,
    # d1/x = 2*(d2/x)

    # Also, Jack cycles 50 miles to Peter at the same speed x
    # Hence, we can say,
    # d1 + d2 + 50 = total distance cycled today

    # Simplifying the first equation we get,
    # d1 = 2*d2

    # Substituting above equation in the second equation we get,
    # 3*d2 + 50 = total distance cycled today

    # Now, we need to find d2, distance from store to Peter
    # Let's assume d2 = y
    # Hence, d1 = 2*y

    # Also given, time taken for d1 is twice the time taken for d2
    # Time taken for d1 = d1/x
    # Time taken for d2 = d2/x
    # 2*(d2/x) = d1/x
    # 2*y/x = 2*d2/x
    # y = d2

    # Simplifying, we get
    # d2 = x*25

    # Substituting above equation in the third equation we get,
    # total distance cycled today = 3*(x*25) + 50
    # total distance cycled today = 75x + 50

    result = "Jack and Peter cycled a total of " + str(75*x + 50) + " miles today."
    return result

print(solution())