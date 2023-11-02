def solution():
    """Owen bought 12 boxes of face masks that cost $9 per box. Each box has 50 pieces of masks. He repacked 6 of these boxes and sold them for $5 per 25 pieces. He sold the remaining 300 face masks in baggies at the rate of 10 pieces of mask for $3. How much profit did he make?"""
    # Define the cost of one box of face masks and the number of pieces it contains
    mask_box_cost = 9
    mask_box_pieces = 50

    # Define the cost of repacking one box of face masks and the number of pieces per repacked bag
    repack_cost = 1.5
    repack_pieces = 25

    # Define the selling price of one bag of repacked face masks and the number of bags repacked
    repack_price = 5
    repack_boxes = 6

    # Define the selling price of one bag of bagged face masks and the number of pieces per bag
    bag_price = 3
    bag_pieces = 10

    # Calculate the total cost of the face masks Owen bought
    total_cost = mask_box_cost * 12

    # Calculate the number of pieces of face masks Owen repacked and sold
    repack_pieces_sold = repack_boxes * repack_pieces

    # Calculate the profit from selling the repacked face masks
    repack_profit = (repack_price / 25) * repack_boxes * repack_pieces - repack_cost * repack_boxes

    # Calculate the number of pieces of face masks Owen sold in baggies
    bag_pieces_sold = 300 - repack_pieces_sold

    # Calculate the profit from selling the bagged face masks
    bag_profit = (bag_price / 10) * bag_pieces_sold - (total_cost - repack_profit)

    # Calculate the total profit
    total_profit = repack_profit + bag_profit

    result = total_profit
    return result

print(solution())