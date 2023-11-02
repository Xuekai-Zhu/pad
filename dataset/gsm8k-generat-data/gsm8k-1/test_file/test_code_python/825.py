def solution():
    """Boris owns a chocolate factory. He produces 50,000 bars of chocolate each month. Boris produces 8,000 bars of chocolate the first week. The second week, Boris only produces half as much as the first week. But, the third week, Boris produces three times as much as the first week. How much does he produce the fourth week?"""
    total_bars_per_month = 50000
    first_week_bars = 8000
    second_week_bars = first_week_bars / 2
    third_week_bars = first_week_bars * 3
    bars_produced_week_four = total_bars_per_month - (first_week_bars + second_week_bars + third_week_bars)
    result = bars_produced_week_four
    return result

print(solution())