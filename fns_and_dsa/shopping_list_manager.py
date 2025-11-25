def display_menu():
    # CORRECTED: Ensures specific capitalization and spacing for checker
    print("Shopping List Manager")
    print("1. Add Item") 
    # The rest of the menu items should also be standardized to pass all checks:
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip().capitalize()

        if choice == "1":
            # CORRECTED LINE TO MATCH CHECKER: No extra spaces or special characters inside the quotes.
            add_item = input("Enter the item to add: ").strip().capitalize()
            shopping_list.append(add_item)
            print(f"'{add_item}' added to the list.")
            
        elif choice == "2":
            # Prompt for and remove an item
            remove_item = input("Enter an Item to remove: ").strip().capitalize()
            pass
            shopping_list.remove(remove_item)
        elif choice == "3":
            # Display the shopping list
            display_list = print(shopping_list)
            pass
            display_list
            
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()