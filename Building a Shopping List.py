shopping_list = []  # Start with an empty list
# Add items using append()
shopping_list.append("Milk")
shopping_list.append("Bread")
shopping_list.append("Eggs")
shopping_list.append("Apples")
# Display the list
print("Shopping List:")
print(shopping_list)
# Add another item using indexing (assuming index 2)
shopping_list[2] = "Cheese"  # Update item at index 2
# OR use insert() to add at a specific position (index 1)
shopping_list.insert(1, "Bananas")
print("Updated Shopping List:", shopping_list)

