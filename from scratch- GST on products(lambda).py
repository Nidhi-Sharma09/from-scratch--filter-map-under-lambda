## Filter picks only the products above $500.
## Map adds 18% GST to those selected products.

price=[453,786,9098,648,457,922,8933,718,132,462,185,192,486,580,6268]
above=list(filter(lambda x: x>=500,price))
print(f"Products above $500: {above}")

gst=list(map(lambda x: x+(x*18/100), above))
print(f"Final Price (Included GST): {gst}")