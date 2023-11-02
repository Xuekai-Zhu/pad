def solution():
    """A carton of ice cream contains 10 scoops each. Mary has 3 cartons of ice cream, one chocolate, one strawberry and one vanilla. Ethan wants one scoop of vanilla and one of chocolate. Lucas, Danny and Connor all want 2 scoops of chocolate. Olivia would like a scoop of vanilla and one of strawberry. Shannon wants twice as much as Olivia. How many scoops of ice cream will be left?"""
    carton_size = 10
    mary_ice_cream = {"chocolate": 1, "strawberry": 1, "vanilla": 1}
    ethan_ice_cream = {"chocolate": 1, "vanilla": 1}
    lucas_ice_cream = {"chocolate": 2}
    danny_ice_cream = {"chocolate": 2}
    connor_ice_cream = {"chocolate": 2}
    olivia_ice_cream = {"vanilla": 1, "strawberry": 1}
    shannon_ice_cream = {"vanilla": 2, "strawberry": 2}
    total_scoops = sum(mary_ice_cream.values()) + sum(ethan_ice_cream.values()) + sum(lucas_ice_cream.values()) + sum(danny_ice_cream.values()) + sum(connor_ice_cream.values()) + sum(olivia_ice_cream.values()) + sum(shannon_ice_cream.values())
    total_scoops_left = (len(mary_ice_cream) * carton_size) - total_scoops
    result = total_scoops_left
    return result

print(solution())