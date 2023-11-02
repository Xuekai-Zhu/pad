def solution():
    """Derek was 6 years old when he had three times as many dogs as cars. Ten years later, after selling some of his dogs and buying 210 more cars, the number of cars became twice the number of dogs. How many dogs does Derek have now if he had 90 dogs when he was six years old?"""
    # Let's assume that when Derek was 6 years old, he had x cars and 3x dogs
    x = 30 # since he had 90 dogs (3x), he must have had 30 cars (x)

    # After 10 years, he sold some dogs and bought 210 more cars
    # Let's assume he sold y dogs and bought 210 cars
    y = 30 # we can solve for y using the fact that he had 3x dogs when he was 6, and now has half as many dogs as cars
    # 3x - y = d (number of dogs he has now)
    # d = 0.5(4(x-y)+210) (since he now has half as many dogs as cars, and has 4 times as many cars as he did when he was 6 - x-y gives us the number of cars he has now)
    d = 180 # plugging in x=30 and y=30 gives us d=180

    # Therefore, Derek now has 180 dogs
    result = d
    return result

print(solution())