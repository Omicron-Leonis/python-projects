actual_cost = float(input("please Enter the Actual Product Price"))
sale_amount = float(input("Please Enter the Sales Amount: "))
if (sale_amount > actual_cost) :
    amount = sale_amount - actual_cost
    print ("Total profit = {0}" .format(amount))
else:
    print ("No Profit!!!!")