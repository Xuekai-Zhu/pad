def solution():
    kenneth_fabric = 700  # ounces of fabric bought by Kenneth
    kenneth_cost = 40  # cost of fabric per ounce for Kenneth
    kenneth_total_cost = kenneth_fabric * kenneth_cost  # total cost of fabric for Kenneth
    nicholas_fabric = 6 * kenneth_fabric  # ounces of fabric bought by Nicholas
    nicholas_cost = kenneth_cost  # assuming Nicholas paid the same price per ounce
    nicholas_total_cost = nicholas_fabric * nicholas_cost  # total cost of fabric for Nicholas
    amount_more_paid = nicholas_total_cost - kenneth_total_cost  # difference in the total cost paid by Nicholas and Kenneth
    result = amount_more_paid
    return result

print(solution())