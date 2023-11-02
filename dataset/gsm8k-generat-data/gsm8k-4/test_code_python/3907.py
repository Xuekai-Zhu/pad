def solution():
    """Melany has to fence a 5000 feet square field with wire mesh. If one foot of wire mesh is sold at $30, and she had $120000, how many feet of the field will not be fenced?"""
    # Define the area of the field and the cost of one foot of wire mesh
    field_area = 5000 ** 2
    cost_per_foot = 30

    # Calculate the total cost of the wire mesh
    total_cost = 120000

    # Calculate the total length of the wire mesh needed
    total_length = total_cost / cost_per_foot

    # Calculate the length of each side of the field
    side_length = field_area ** 0.5

    # Calculate the total length of the fence needed
    total_fence_length = side_length * 4

    # Calculate the length of the field that will not be fenced
    unfenced_length = total_fence_length - total_length

    result = unfenced_length
    return result

print(solution())