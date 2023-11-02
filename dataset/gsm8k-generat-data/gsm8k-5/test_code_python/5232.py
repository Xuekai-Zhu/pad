def solution():
    # Let's assume that Jill used x amount of each scent for one candle
    # Jill made twice as many lavender candles as coconut candles, so let's assume she made y coconut candles
    y = 1  # We know that she made at least one batch of coconut candles
    x = y / 2  # She made twice as many lavender candles as coconut candles
    # Since she ran out of almond scent after making 10 candles
    # And she used the same amount of each scent for every candle, we know that 10x = the amount of almond scent she had
    almond_scent = 10*x
    # Jill had one and a half times as much coconut scent as almond scent
    # So her coconut scent would be 1.5*almond_scent
    coconut_scent = 1.5*almond_scent
    # Since Jill used the same amount of each scent for every candle, she could make a total of (almond_scent + coconut_scent + 2*y*x) candles
    # And we know that she made 10 almond candles, so she made (almond_scent - 10*x)/x batches of lavender and coconut candles
    # This simplifies to (almond_scent/x) - 10 batches of lavender and coconut candles
    # And we know that coconut scent was 1.5 times almond scent, so almond_scent/x = 2*coconut_scent/y
    # Substituting this equation gives us 2*coconut_scent/y - 10 batches of lavender and coconut candles
    # We can further simplify this to 2*(1.5*almond_scent)/y - 10 batches of lavender and coconut candles
    # Substituting our values gives us 2*(1.5*(10*x))/y - 10 = 2*(15*x)/y - 10
    # We know that this number of batches equals the number of lavender candles Jill made, which is 2*y*x
    # So let's set 2*y*x = 2*(15*x)/y - 10 and solve for y
    # 2*y*x + 10 = 2*(15*x)/y
    # y(2*y*x + 10) = 2*15*x
    # 2*y^2*x + 10*y - 30*y*x = 0
    # 2*y^2*x - 20*y*x + 10*y = 0
    # 2yx(y - 10) + 5y = 0
    # y(2yx + 5) = 0
    # y = 0 (this value doesn't make sense) or y = -5/(2x) (this is negative, so it doesn't make sense either)
    # Therefore, y must be positive, so y = 5/x
    y = 5/x
    # And we know that she made twice as many lavender candles as coconut candles, so she made 2*y*x lavender candles
    lavender_candles = 2*y*x
    result = lavender_candles
    return result

print(solution())