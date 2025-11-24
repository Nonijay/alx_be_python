def display_menu():
    print ("\n----Shopping List Manager----")
    print (" 1. Add Item")
    print (" 2. Remove Item")
    print (" 3. View List")
    print (" 4. Exit")
    print("---------------")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip().capitalize()

        if choice == "1":
            # Prompt for and add an item
            add_item = input("Add an Item: ")
            pass 
            shopping_list.append(add_item)
            print("Item added successfully")
            
        elif choice == "2":
            # Prompt for and remove an item
            remove_item = input("Enter an Item to remove: ")
            pass
            shopping_list.remove()
        elif choice == "3":
            # Display the shopping list
            display_list = print(shopping_list)
            return display_list
            pass
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()