class FamilyMember:
    def __init__(self, name, family_name, birthdate):
        self.name = name
        self.family_name = family_name
        self.birthdate = birthdate
        self.children = []

def add_family_member(parent, name, family_name, birthdate):
    new_member = FamilyMember(name, family_name, birthdate)
    parent.children.append(new_member)
    return new_member

def get_sorted_birthdays(root):
    birthdays = []
    traverse_and_fill_birthdays(root, birthdays)
    return sorted(birthdays, key=lambda x: x[1])

def traverse_and_fill_birthdays(node, birthdays):
    if node:
        birthdays.append((f"{node.name} {node.family_name}", node.birthdate))
        for child in node.children:
            traverse_and_fill_birthdays(child, birthdays)

def find_relationship(node1, node2):
    if node2 in node1.children:
        return "Child"
    elif node1 in node2.children:
        return "Parent"
    else:
        return "Not directly related"

def visualize_family_tree(root, level=0):
    if root:
        print("  " * level + f"{root.name} {root.family_name} - {root.birthdate}")
        for child in root.children:
            visualize_family_tree(child, level + 1)

def count_same_first_names(root, first_name):
    count = 0
    traverse_and_count_names(root, first_name, count)
    return count

def traverse_and_count_names(node, first_name, count):
    if node:
        if node.name.split()[0] == first_name:
            count += 1
        for child in node.children:
            traverse_and_count_names(child, first_name, count)


root = FamilyMember("John Doe", "Doe", "1990-01-01")

while True:
    print("- - - - - - - - - - - - - - -")
    print("1. Add Family Member")
    print("2. Display Sorted Birthdays")
    print("3. Find Relationship")
    print("4. Visualize Family Tree")
    print("5. Count Same First Names")
    print("6. Exit")
    
    choice = int(input("Choice: "))

    if choice == 1:
        parent_name = input("Parent's full name: ")
        parent = find_member_by_name(root, parent_name)
        if parent:
            name = input("New member's full name: ")
            family_name = input("Family name: ")
            birthdate = input("Birthdate (YYYY-MM-DD): ")
            add_family_member(parent, name, family_name, birthdate)
            print("Family member added successfully.")
        else:
            print("Parent not found.")

    elif choice == 2:
        sorted_birthdays = get_sorted_birthdays(root)
        print("Sorted Birthdays:")
        for member, birthday in sorted_birthdays:
            print(f"{member} - {birthday}")

    elif choice == 3:
        name1 = input("First member's full name: ")
        name2 = input("Second member's full name: ")
        member1 = find_member_by_name(root, name1)
        member2 = find_member_by_name(root, name2)
        if member1 and member2:
            relationship = find_relationship(member1, member2)
            print(f"Relationship: {relationship}")
        else:
            print("One or both members not found.")

    elif choice == 4:
        visualize_family_tree(root)

    elif choice == 5:
        first_name = input("Enter first name: ")
        count = count_same_first_names(root, first_name)
        print(f"Count of family members with the first name '{first_name}': {count}")

    elif choice == 6:
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please enter a valid option.")
