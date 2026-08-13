import csv


def menu():
    print("\n===== SALES ANALYZER =====")
    print("1. View sales")
    print("2. Calculate total sales")
    print("3. Find the best-selling product")
    print("4. Show sales by category")
    print("5. Exit")


def load_sales():
    sales = []

    try:
        with open("sales.csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            for row in reader:
                sales.append(row)

    except FileNotFoundError:
        print("Sales file not found.")

    return sales


def view_sales():
    if not sales:
        print("No sales found.")
        return

    print("\n===== SALES =====")

    for sale in sales:
        print(f"Product: {sale['product']}")
        print(f"Category: {sale['category']}")
        print(f"Quantity: {sale['quantity']}")
        print(f"Price: €{sale['price']}")
        print("--------------------")


def calculate_total_sales():
    if not sales:
        print("No sales found.")
        return

    total = 0

    for sale in sales:
        quantity = int(sale["quantity"])
        price = float(sale["price"])

        total += quantity * price

    print(f"Total sales: €{total:.2f}")


def best_selling_product():
    if not sales:
        print("No sales found.")
        return

    best_product = None
    highest_quantity = 0

    for sale in sales:
        quantity = int(sale["quantity"])

        if quantity > highest_quantity:
            highest_quantity = quantity
            best_product = sale["product"]

    print(f"Best-selling product: {best_product}")
    print(f"Units sold: {highest_quantity}")


def sales_by_category():
    if not sales:
        print("No sales found.")
        return

    category_totals = {}

    for sale in sales:
        category = sale["category"]
        quantity = int(sale["quantity"])
        price = float(sale["price"])

        total = quantity * price

        if category in category_totals:
            category_totals[category] += total
        else:
            category_totals[category] = total

    print("\n===== SALES BY CATEGORY =====")

    for category, total in category_totals.items():
        print(f"{category}: €{total:.2f}")


sales = load_sales()

print(f"Loaded {len(sales)} sales.")


while True:
    menu()

    option = input("Choose an option: ")

    if option == "1":
        view_sales()

    elif option == "2":
        calculate_total_sales()

    elif option == "3":
        best_selling_product()

    elif option == "4":
        sales_by_category()

    elif option == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")
