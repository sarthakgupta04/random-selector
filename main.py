import random

def display_menu():
    print("\nMenu:")
    print("1. Add a category")
    print("2. Add items to a category")
    print("3. Select a random item from a category")
    print("4. Display all categories and items")
    print("5. Exit")

def add_category(categories):
    if len(categories) >= 5:
        print("Maximum of 5 categories reached.")
        return
    category_name = input("Enter category name: ").strip()
    if category_name in categories:
        print("Category already exists.")
    else:
        categories[category_name] = []
        print(f"Category '{category_name}' added.")

def add_items(categories):
    if not categories:
        print("No categories available. Add a category first.")
        return
    category_name = input("Enter category name: ").strip()
    if category_name not in categories:
        print("Category does not exist.")
        return
    current_item_count = len(categories[category_name])
    remaining_space = 10 - current_item_count
    if remaining_space <= 0:
        print("Maximum of 10 items already reached in this category.")
        return

    print(f"You can add up to {remaining_space} items.")
    items_input = input(f"Enter items separated by commas (at least 1 and up to {remaining_space}): ").strip()
    items = [item.strip() for item in items_input.split(",") if item.strip()]

    if len(items) < 1 or len(items) > remaining_space:
        print(f"Invalid number of items. You must enter at least 1 and up to {remaining_space} items.")
        return
    
    categories[category_name].extend(items)
    print(f"Items added to category '{category_name}': {', '.join(items)}")

def select_random_item(categories):
    if not categories:
        print("No categories available.")
        return
    category_name = input("Enter category name: ").strip()
    if category_name not in categories:
        print("Category does not exist.")
        return
    if not categories[category_name]:
        print("No items in this category.")
        return
    random_item = random.choice(categories[category_name])
    categories[category_name].remove(random_item)
    print(f"Random item from '{category_name}': {random_item} (removed from category)")

def display_categories(categories):
    if not categories:
        print("No categories available.")
        return
    for category, items in categories.items():
        print(f"\nCategory: {category}")
        for item in items:
            print(f"  - {item}")

def main():
    print("Starting Randomizer Program...")
    categories = {}
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_category(categories)
        elif choice == "2":
            add_items(categories)
        elif choice == "3":
            select_random_item(categories)
        elif choice == "4":
            display_categories(categories)
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
