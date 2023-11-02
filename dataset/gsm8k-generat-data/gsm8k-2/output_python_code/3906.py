def solution():
    """Melany has to fence a 5000 feet square field with wire mesh. If one foot of wire mesh is sold at $30, and she had $120000, how many feet of the field will not be fenced?"""
    field_perimeter = 4 * 5000 ** 0.5
    wire_cost_per_foot = 30
    total_wire_cost = field_perimeter * wire_cost_per_foot
    remaining_money = 120000 - total_wire_cost
    unfenced_area = (remaining_money / wire_cost_per_foot) ** 2
    unfenced_perimeter = 4 * unfenced_area ** 0.5
    unfenced_length = unfenced_perimeter / 2  # since the field is a square
    result = 5000 - unfenced_length
    return result

print(solution())