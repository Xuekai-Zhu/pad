def solution():
    """Marcel runs a bicycle store. His main products are three types of bikes: MTB, BMX, and Trekking. The price of one MTB is $500, BMX is half the price of an MTB, and a Trekking bike is $450. In one month, Marcel sold a total of 300 bikes among the types listed. Half of them were Trekking bikes, and 15% were BMX bikes. The rest of the sold bikes were MTB type. How much did Marcel earn from selling bicycles during that month?"""
    mtb_price = 500
    bmx_price = mtb_price / 2
    trekking_price = 450
    total_bikes_sold = 300
    trekking_bikes_sold = total_bikes_sold / 2
    bmx_bikes_sold = total_bikes_sold * 0.15
    mtb_bikes_sold = total_bikes_sold - trekking_bikes_sold - bmx_bikes_sold
    total_profit = (mtb_bikes_sold * mtb_price) + (bmx_bikes_sold * bmx_price) + (trekking_bikes_sold * trekking_price)
    result = total_profit
    return result

print(solution())