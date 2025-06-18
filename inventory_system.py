class InventorySystem:
    def __init__(self):
        # Initialize with some sample stock items
        self.inventory = {
            "Laptops": 10,
            "Monitors": 15,
            "Keyboards": 20,
            "Mice": 25,
            "Headphones": 30
        }

    def display_inventory(self):
        if not self.inventory:
            return print("\nInventory is empty!")
        
        print("\nCurrent Inventory:")
        print("-" * 50)
        print(f"{'Item Name':<20} {'Quantity':<10} {'Status':<15}")
        print("-" * 50)
        
        # Using a loop to display items with status
        for item, quantity in self.inventory.items():
            status = "Low Stock" if quantity < 15 else "In Stock" if quantity < 25 else "Well Stocked"
            print(f"{item:<20} {quantity:<10} {status:<15}")

    def display_low_stock(self):
        print("\nLow Stock Items (Less than 15 units):")
        print("-" * 40)
        # Loop to find and display low stock items
        low_stock = {item: qty for item, qty in self.inventory.items() if qty < 15}
        if low_stock:
            for item, quantity in low_stock.items():
                print(f"{item:<20} {quantity:<10}")
        else:
            print("No low stock items found.")

    def update_stock_levels(self):
        print("\nUpdating Stock Levels:")
        print("-" * 40)
        # Loop through all items to update quantities
        for item in self.inventory:
            try:
                new_qty = int(input(f"Enter new quantity for {item} (current: {self.inventory[item]}): "))
                if new_qty >= 0:
                    self.inventory[item] = new_qty
                    print(f"Updated {item} quantity to {new_qty}")
                else:
                    print("Quantity cannot be negative. Update skipped.")
            except ValueError:
                print("Invalid input. Update skipped.")

    def validate_quantity(self, quantity):
        try:
            qty = int(quantity)
            return qty if qty >= 0 else None
        except ValueError:
            return None

    def manage_item(self, item_name, quantity=None, action='add'):
        if action == 'remove':
            return self.inventory.pop(item_name, None) and print(f"\nRemoved {item_name} from inventory") or print(f"\nError: {item_name} not found!")
        
        qty = self.validate_quantity(quantity)
        if qty is None:
            return print("Error: Invalid quantity!")
        
        if action == 'add':
            self.inventory[item_name] = self.inventory.get(item_name, 0) + qty
            print(f"\n{'Updated' if item_name in self.inventory else 'Added'} {item_name} quantity to {self.inventory[item_name]}")
        elif action == 'update':
            if item_name in self.inventory:
                self.inventory[item_name] = qty
                print(f"\nUpdated {item_name} quantity to {qty}")
            else:
                print(f"\nError: {item_name} not found!")

    def search_item(self, item_name):
        print(f"\nFound {item_name}: Quantity = {self.inventory[item_name]}" if item_name in self.inventory else f"\n{item_name} not found in inventory")

def main():
    inventory = InventorySystem()
    menu = {
        '1': ('Display All Inventory', lambda: inventory.display_inventory()),
        '2': ('Display Low Stock Items', lambda: inventory.display_low_stock()),
        '3': ('Update All Stock Levels', lambda: inventory.update_stock_levels()),
        '4': ('Add/Update Single Item', lambda: inventory.manage_item(input("Enter item name: "), input("Enter quantity: "), 'add')),
        '5': ('Remove Item', lambda: inventory.manage_item(input("Enter item name to remove: "), action='remove')),
        '6': ('Search Item', lambda: inventory.search_item(input("Enter item name to search: "))),
        '7': ('Exit', lambda: print("\nThank you for using the Inventory Management System!") or exit())
    }
    
    while True:
        print("\n=== Inventory Management System ===")
        [print(f"{k}. {v[0]}") for k, v in menu.items()]
        choice = input("\nEnter your choice (1-7): ")
        menu.get(choice, (None, lambda: print("\nInvalid choice! Please try again.")))[1]()

if __name__ == "__main__":
    main() 