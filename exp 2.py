import numpy as np

sales = np.array([
    [100, 150, 200],
    [250, 300, 350],
    [120, 180, 240]
])

average_price = np.mean(sales)

print("Average price of all products:", average_price)
