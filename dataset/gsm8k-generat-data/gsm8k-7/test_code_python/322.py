def solution():
    total_bill = 140
    sales_tax_rate = 0.1
    entree_price = 80
    wine_price = 10

    # Calculate the sales tax on the entree and wine
    sales_tax = (entree_price + wine_price) * sales_tax_rate

    # Calculate the subtotal of the entree and wine before gratuity
    subtotal = entree_price + wine_price + sales_tax

    # Calculate the total gratuity charged by the restaurant
    gratuity = total_bill - subtotal

    result = gratuity
    return result

print(solution())