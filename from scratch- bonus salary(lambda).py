# Filter picks only the employees with salaries above $4000.
# Map adds a 10% bonus to those selected employees.

salary=[5358,1573,4829,5725,1523,1369,4280.3679,3800,2794]
above=list(filter(lambda x: x>4000, salary))
print(f"Salary abole #4000: {above}")

bouns=list(map(lambda x: x+(x*10/100),above))
print(f"salary including bonus: {bouns}")
