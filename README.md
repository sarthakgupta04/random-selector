Problem Statement: Randomizer Menu

Design a class RandomizerMenu to implement a randomizer program with the following functionalities:

  add_category(name): Adds a new category with the given name to the menu. The menu can hold up to 5 categories. If the maximum limit is reached, print "Maximum of 5 categories reached."
  
  add_items(category_name, items): Adds items to the specified category. Each category can hold up to 10 items. If the maximum limit is reached, print "Maximum of 10 items already reached in this category."
  
  select_random_item(category_name): Selects a random item from the specified category. If the category does not exist or has no items, print the appropriate message. Returns the selected item and removes it from the category.
  
  display_categories(): Displays all categories and their items.

Implement the RandomizerMenu class and a sample usage demonstrating its functionalities.
