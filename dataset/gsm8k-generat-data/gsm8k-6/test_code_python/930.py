def solution():
    # Let's call the number of apples each woman bought "w"
    # Then, we know that each man bought 30 apples and each woman bought w apples
    # We also know that each man bought 20 fewer apples than each woman
    # So, we can write the following equation: 2*30 + 3*w = 3*(w+20)
    # Solving for w, we get w = 40
    # Therefore, each woman bought 40 apples and the total number of apples bought is 2*30 + 3*40 = 150
    result = 150
    return result

print(solution())