def solution():
    """Naruto can lift a mountain ten times higher than Kagiyami can. But Kagiyami can lift a mountain 4 times higher than Saskay can. And Saskay can lift a mountain 12 times higher than Pompei can. If Pompei can lift a mountain 1 inch, how high can Naruto lift a mountain, in feet?"""
    pompei_lift = 1 # in inches
    saskay_mult = 12
    kagiyami_mult = 4
    naruto_mult = 10
    saskay_lift = pompei_lift * saskay_mult # in inches
    kagiyami_lift = (pompei_lift * saskay_mult) * kagiyami_mult # in inches
    naruto_lift = (pompei_lift * saskay_mult * kagiyami_mult * naruto_mult) / 12 # convert to feet
    result = naruto_lift
    return result

print(solution())