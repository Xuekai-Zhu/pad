def solution():
    """Greta wanted brownies for her birthday. She made a batch for herself; one dozen cream cheese swirl brownies. 
    At her office, they threw her a party and sent her home with 1/2 a dozen brownies. When she arrived home, 
    her friends were there to throw her a surprise party and had 4 dozen brownies waiting. During the party, 
    1 1/2 dozen brownies were eaten. How many individual brownies did Greta have left over from the entire day?"""
    self_made = 12
    office_party = 6
    surprise_party = 4 * 12
    eaten_at_party = 1.5 * 12
    total_brownies = self_made + office_party + surprise_party - eaten_at_party
    result = total_brownies
    return result

print(solution())