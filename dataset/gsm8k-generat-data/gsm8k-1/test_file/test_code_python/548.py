def solution():
    """A marketing company pays its employees on a commission-based salary system. If you sell goods worth $1000, you earn a 30% commission. Sales over $1000 get you an additional 10% commission. Calculate the amount of money Antonella earned if she sold goods worth $2500."""
    sale_price = 2500
    commission_rate1 = 0.3
    commission_rate2 = 0.1
    commission1 = 1000 * commission_rate1
    commission2 = (sale_price - 1000) * commission_rate2
    total_commission = commission1 + commission2
    earnings = total_commission
    return earnings

print(solution())