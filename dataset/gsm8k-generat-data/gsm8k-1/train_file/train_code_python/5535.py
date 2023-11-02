def solution():
    """Maya's organization hosted a weekly farmers' market to raise money for the church choir. They sold broccolis, carrots, spinach, and cauliflowers. After adding together all of their earnings, Maya found out that they had made $380. The organization made $57 from broccoli and the sales of the carrots are twice as much as the sales of broccoli. Then, their sales for the spinach is $16 more than half of the sales of carrots. How much did they make from cauliflower sales?"""
    total_earnings = 380
    earnings_broccoli = 57
    earnings_carrots = 2 * earnings_broccoli
    earnings_spinach = earnings_carrots / 2 + 16
    earnings_cauliflower = total_earnings - earnings_broccoli - earnings_carrots - earnings_spinach
    result = earnings_cauliflower
    return result

print(solution())