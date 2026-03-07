import csv

def show_menu():
    print("""
╔════════════════════════════════════════╗
║       🛒  TECH INVENTORY SYSTEM        ║
╠════════════════════════════════════════╣
║  1. Show products                      ║
║  2. Add product                        ║
║  3. Edit product                       ║
║  4. Delete product                     ║
║  5. Exit                               ║
╚════════════════════════════════════════╝
    """)

def load_csv(filename):
    inventory = []
    try:
        with open(filename, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                inventory.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "brand": row["brand"],
                    "amount": int(row["amount"]),
                    "price": float(row["price"])
                })
    except FileNotFoundError:
        pass

    return inventory

def save_csv(inventory, filename):
    with open(filename, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "name", "brand", "amount", "price"])
        writer.writeheader()
        writer.writerows(inventory)

def show_products(inventory):
    if not inventory:
        print("There are no products in inventory.")
        return

    name_w  = max(len(p["name"])  for p in inventory)
    brand_w = max(len(p["brand"]) for p in inventory)

    top    = f"╔════╦{'═'*(name_w+2)}╦{'═'*(brand_w+2)}╦══════════╦══════════╗"
    header = f"║ ID ║ {'Name':<{name_w}} ║ {'Brand':<{brand_w}} ║ Amount   ║ Price    ║"
    mid    = f"╠════╬{'═'*(name_w+2)}╬{'═'*(brand_w+2)}╬══════════╬══════════╣"
    bot    = f"╚════╩{'═'*(name_w+2)}╩{'═'*(brand_w+2)}╩══════════╩══════════╝"

    print(top)
    print(header)
    print(mid)
    for p in inventory:
        print(f"║ {p['id']:<3}║ {p['name']:<{name_w}} ║ {p['brand']:<{brand_w}} ║ {p['amount']:<9}║ {p['price']:<9}║")
    print(bot)



def add_products(inventory, name, brand, amount, price):
    new_product = {
        "id": max((p["id"] for p in inventory), default=0) + 1,
        "name": name,
        "brand": brand,
        "amount": amount,
        "price": price
    }

    inventory.append(new_product)

def update(inventory, id_update):
    
    product = None
    for p in inventory:
        if p["id"] == id_update:
            product = p
            break
    
    if product is None:
        print("ID does not exist")
        return inventory

    while True:
        option = input("""
        What field do you want to modify??:
            1) Name
            2) Brand
            3) Amount
            4) Price
            5) Return to menú
        """)

        if option == "1":
                product["name"] = input("New name: ")
        elif option == "2":
                product["brand"] = input("New brand: ")
        elif option == "3":
                product["amount"] = get_int("New amount: ")
        elif option == "4":
                product["price"] = get_float("New price: ")
        else:
                break
    
    return inventory
    

def delete(inventory, id_to_delete):
    return [p for p in inventory if p["id"] != id_to_delete]

def get_int(prompt):
     while True:
          try:
               return int(input(prompt).strip())
          except ValueError:
               print("Enter a valid number.")

def get_float(prompt):
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
             print("Enter a valid number")



def main():
    inventory = load_csv("inventory.csv")


    while True:
        show_menu()
        option = input("  >>> Choose an option: ")

        if option == "1":
            show_products(inventory)
        elif option == "2":
            name = input("Name: ").strip()
            brand = input("Brand: ").strip()
            amount = get_int("Amount: ")
            price = get_float("Price: ")
            add_products(inventory, name, brand, amount, price)
            save_csv(inventory, "inventory.csv")      
        elif option == "3":
            id_update = get_int("ID to update: ")
            inventory = update(inventory, id_update)
            save_csv(inventory, "inventory.csv") 
        elif option == "4":
            id_to_delete = get_int("ID to delete: ")
            inventory = delete(inventory, id_to_delete)
            save_csv(inventory, "inventory.csv") 
        elif option == "5":
            break

if __name__ == "__main__":
    main()