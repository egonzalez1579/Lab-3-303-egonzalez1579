"""
Author: Edwin Gonzalez Mendoza
Date: 2025-01-26

This program simulates a simple shopping cart.
Users can add items, specify quantities, and see the total cost.
The program uses exception handling to manage invalid inputs.
Additionally, if the total cost exceeds $100, a 10% discount is applied.
"""


def main():
    cart = []  #List to store the items in the shopping cart.
    print("Welcome to the shopping cart program!")


    while True:
        try:
            # Input details for the product.
            description = input("Enter a description of the product: ") # Product description.
            quantity = int(input("Enter the quantity: ")) # Number of units of the product.
            price = float(input("Enter the price per unit: ")) # Price per unit of the product.

            total_cost = quantity * price # Total cost for this product.
            cart.append((description, quantity, price, total_cost)) # Add product details to the cart.

            print(f"Added {quantity} x {description} at ${price:.2f} each. Total: ${total_cost:,.2f}")

            # Ask if the user wants to start over or quit.
            restart = input("Would you like to add another item? (yes/no): ").strip().lower()
            if restart != 'yes':
                break
        except ValueError:
            # Handle invalid input for quantity or price.
            print("Invalid input. Please enter numeric values for quantity and price.")

    # Display the shopping cart summary.
    print("\nShopping Cart Summary:")
    grand_total = 0  # Total cost of all items in the cart.
    for item in cart:
        print(f"{item[1]} x {item[0]} at ${item[2]:.2f} each. Total: ${item[3]:,.2f}")
        grand_total += item[3]  # Accumulate the total cost of all products.

    # Apply a discount if the total cost exceeds $100.
    if grand_total > 100:
        discount = grand_total * 0.1 # Calculate 10% discount.
        grand_total -= discount  # Subtract the discount from the grand total.
        print(f"\nYou saved ${discount:,.2f} with a 10% discount!")
        print(f"Discounted Total: ${grand_total:,.2f}")   # Display the grand total.
    else:
        print(f"\nGrand Total: ${grand_total:.2f}")   # Display the grand total.


main()
