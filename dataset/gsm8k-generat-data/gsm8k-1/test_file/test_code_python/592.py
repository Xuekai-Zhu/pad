def solution():
    """George needs to pay for dental work. He needs 2 implants. Each implant has a base price of $2000. For one of the implants, he wants a crown made of porcelain. That feature costs an extra $500. He’s already put down a deposit of $600. He makes $15 per hour at work. How many hours does he need to work before he has enough to pay for the dental work?"""
    num_implants = 2
    base_price = 2000
    porcelain_cost = 500
    deposit = 600
    total_cost = (num_implants * base_price) + porcelain_cost - deposit
    hourly_wage = 15
    hours_needed = total_cost / hourly_wage
    result = hours_needed
    return result

print(solution())