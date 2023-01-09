meal_price = int(input("Enter meal price : "));
tax = int(input("Enter tax percentage : "));
tip = int(input("Enter the tip pecentage : "));
tax_amount = meal_price * (tax/100);
tip_amount = (meal_price + tax_amount)*(tip/100);
total_amount = meal_price + tax_amount + tip_amount;
print("The total bill is ${}".format("%.2f" %total_amount));
