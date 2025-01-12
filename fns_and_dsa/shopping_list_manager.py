def display_menu():
    """Displays the menu with options to the user."""
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def add_item(shopping_list):
    """Prompts the user to add an item to the shopping list."""
    item = input("Enter the name of the item to add: ").strip()
    if item:
        shopping_list.append(item)
        print(f'"{item}" has been added to the shopping list.')
    else:
        print("Item name cannot be empty.")

def remove_item(shopping_list):
    """Prompts the user to remove an item from the shopping list."""
    item = input("Enter the name of the item to remove: ").strip()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f'"{item}" has been removed from the shopping list.')
    else:
        print(f'"{item}" is not in the shopping list.')

def view_list(shopping_list):
    """Displays the current shopping list."""
    if shopping_list:
        print("\nCurrent Shopping List:")
        for idx, item in enumerate(shopping_list, start=1):
            print(f"{idx}. {item}")
    else:
        print("The shopping list is empty.")

def main():
    """Main function to manage the shopping list."""
    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            remove_item(shopping_list)
        elif choice == '3':
            view_list(shopping_list)
        elif choice == '4':
            print("Exiting the Shopping List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
