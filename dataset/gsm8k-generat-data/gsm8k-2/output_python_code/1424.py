def solution():
    """Betty and Dora started making some cupcakes at the same time. Betty makes 10 cupcakes every hour and Dora makes 8 every hour. If Betty took a two-hour break, what is the difference between the number of cupcakes they made after 5 hours?"""
    betty_cupcakes = 10 * 3
    dora_cupcakes = 8 * 5
    total_cupcakes = betty_cupcakes + dora_cupcakes
    betty_break_cupcakes = 10 * 2
    final_betty_cupcakes = betty_cupcakes + betty_break_cupcakes
    difference = final_betty_cupcakes - dora_cupcakes
    result = difference
    return result

print(solution())