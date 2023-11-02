def solution():
    """44 seniors need to receive awards. Each senior receives a picture frame that costs $20. Each picture frame needs to be etched with the logo for an additional 20% cost per frame. 2 of the seniors will also receive pins that are $5. 1/4 of the seniors are officers and they will need to receive cords that are $12 each. How much will be spent on the senior gifts?"""
    num_seniors = 44
    frame_cost = 20
    logo_cost = frame_cost * 0.2
    total_frame_cost = (frame_cost + logo_cost) * num_seniors
    pin_cost = 5 * 2
    num_officers = num_seniors // 4
    cord_cost = 12
    total_cord_cost = cord_cost * num_officers
    total_cost = total_frame_cost + pin_cost + total_cord_cost
    result = total_cost
    return result

print(solution())