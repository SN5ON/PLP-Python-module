
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_price = price - (price * (discount_percent / 100))
        return discount_price
    else:
        return price
    
original_price = float(input("Enter original price of an item: "))
discount_percent = float(input("Discounted percentage: "))

final_price = calculate_discount(original_price, discount_percent)
if final_price == original_price:
    print(f"No discount applied. The original price is: ${final_price:.2f}")
else:
    print(f"The final price after a {discount_percent}% discount is: ${final_price:.2f}")