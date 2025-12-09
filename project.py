menu = {
    1: ("Burger", 5.0),
    2: ("Fries", 2.5),
    3: ("Soda", 1.5),
    4: ("Salad", 4.0),
    5: ("Pizza Slice", 3.5)
}

def display_menu():
    print("\nMenu:")
    for k, v in menu.items():
        print(f"{k}. {v[0]} - ${v[1]:.2f}")

def add_item(order):
    try:
        i = int(input("Enter item number to add: "))
        if i not in menu:
            print("Invalid item.")
            return
        q = int(input("Quantity: "))
        if q <= 0:
            print("Quantity must be > 0.")
            return
        name, price = menu[i]
        for it in order:
            if it["id"] == i:
                it["qty"] += q
                print(f"Added {q} x {name} (now {it['qty']})")
                return
        order.append({"id": i, "name": name, "price": price, "qty": q})
        print(f"Added {q} x {name}")
    except ValueError:
        print("Please enter numbers only.")

def remove_item(order):
    if not order:
        print("Order is empty.")
        return
    try:
        i = int(input("Enter item number to remove (or 0 to cancel): "))
        if i == 0:
            return
        for it in order:
            if it["id"] == i:
                q = int(input("Quantity to remove: "))
                if q >= it["qty"]:
                    order.remove(it)
                    print(f"Removed {it['name']} from order.")
                else:
                    it["qty"] -= q
                    print(f"Removed {q} of {it['name']} (now {it['qty']})")
                return
        print("Item not in order.")
    except ValueError:
        print("Please enter numbers only.")

def view_order(order):
    if not order:
        print("Order is empty.")
        return
    total = 0
    print("\nCurrent order:")
    for it in order:
        line = it["qty"] * it["price"]
        total += line
        print(f"{it['name']} x{it['qty']} = ${line:.2f}")
    print(f"Total: ${total:.2f}")

def checkout(order):
    if not order:
        print("Nothing to checkout.")
        return
    view_order(order)
    name = input("Enter customer name: ").strip()
    print(f"Thank you, {name}. Order placed.")
    order.clear()

def main():
    order = []
    while True:
        print("\n1) Show menu  2) Add item  3) Remove item  4) View order  5) Checkout  6) Quit")
        choice = input("Choose: ").strip()
        if choice == "1":
            display_menu()
        elif choice == "2":
            display_menu()
            add_item(order)
        elif choice == "3":
            view_order(order)
            remove_item(order)
        elif choice == "4":
            view_order(order)
        elif choice == "5":
            checkout(order)
        elif choice == "6":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
