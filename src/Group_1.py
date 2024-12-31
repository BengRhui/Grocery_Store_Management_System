# Group 1


def write_inventory_to_file():

    """This function appends the items in the lists to the inventory.txt"""

    file = open("inventory.txt", "w")
    temp_list = []
    for num in range(len(code_list)):
        temp_list.append(f'{code_list[num]:10}{description_list[num]:30}'
                         f'{category_list[num]:15}{str(unit_list[num]):15}'
                         f'{format(price_list[num], ".2f"):10}'
                         f'{str(quantity_list[num]):10}'
                         f'{str(threshold_list[num]):10}\n')
    temp_list.sort()
    for lists in temp_list:
        file.writelines(lists)


def append_file_to_inventory():

    """This function appends the items in inventory.txt to the empty lists (for inventory)."""

    file = open("inventory.txt", "r")
    lines = file.readlines()
    for line in lines:
        field = line.split()
        code_list.append(field[0])
        description_list.append(field[1])
        category_list.append(field[2])
        unit_list.append(field[3])
        price_list.append(float(field[4]))
        quantity_list.append(int(field[5]))
        threshold_list.append(int(field[6]))
    file.close()


def clear_inventory():

    """This function clears all the data inside the lists (for lists related to inventory)."""

    code_list.clear()
    description_list.clear()
    category_list.clear()
    unit_list.clear()
    price_list.clear()
    quantity_list.clear()
    threshold_list.clear()


def write_user_to_file():

    """This function appends the elements from the lists (for users) to username.txt"""

    file = open("username.txt", "w")
    for name in range(len(user_list)):
        file.writelines(f'{user_list[name]:25}'
                        f'{password_list[name]:25}'
                        f'{usertype_list[name]:20}\n')
    file.close()


def append_file_to_user():

    """This function adds users from the username.txt file to empty lists (for users)."""

    file = open("username.txt", "r")
    lines = file.readlines()
    for line in lines:
        field = line.split()
        user_list.append(field[0])
        password_list.append(field[1])
        usertype_list.append(field[2])
    file.close()


def clear_user():

    """This function deletes all the elements in the list (for users)."""

    user_list.clear()
    password_list.clear()
    usertype_list.clear()


def insert_to_list():

    """This function is used to insert new items to empty lists (for inventory)."""

    print("\nWelcome to the interface for inserting new item. "
          "\nNote: Item code must consists only numbers.")

    while True:
        while True:
            code = input("\nEnter the item code: ")
            if code == "":
                print("You did not enter any value.\n")
                while True:
                    decision = input("Do you wish to terminate (y/n): ").lower()
                    if decision == "y":
                        return
                    elif decision == "n":
                        break
                    else:
                        print("Invalid input. Please key in again.\n")
                        continue
                continue
            elif code in code_list:
                print("The code has been used for another item. Please use another code.")
                continue
            else:
                try:
                    int(code)
                except ValueError:
                    print("The code does not satisfy the requirements. Please try again.")
                    continue
                else:
                    code_list.append(code)
                    break

        while True:
            description = "_".join(input("\nEnter the item description: ").title().split())
            if description == "":
                print("You have not entered any value.\n")
                while True:
                    decision = input("Do you wish to terminate (y/n): ").lower()
                    if decision == "y":
                        code_list.pop(len(code_list) - 1)
                        return
                    elif decision == "n":
                        break
                    else:
                        print("Invalid value. Please key in again.\n")
                        continue
            elif description in description_list:
                position = description_list.index(description) + 1
                print("\nThe item is at number %d of the list, with the item code %d."
                      % (position, int(code_list[description_list.index(description)])))
                print("Please go to the 'Modify' section to modify the data, or key in another description.\n")
                while True:
                    decision = input("Do you wish to terminate (y/n): ").lower()
                    if decision == "y":
                        code_list.pop(len(code_list) - 1)
                        return
                    elif decision == "n":
                        break
                    else:
                        print("Invalid input. Please key in again.\n")
                        continue
            else:
                description_list.append(description)
                break

        while True:
            category = input("\nEnter the item category: ").lower()
            if category == "":
                print("You have not entered any value.\n")
                while True:
                    decision = input("Do you wish to terminate (y/n): ").lower()
                    if decision == "y":
                        code_list.pop(len(code_list) - 1)
                        description_list.pop(len(description_list) - 1)
                        return
                    elif decision == "n":
                        break
                    else:
                        print("Invalid input. Please key in again.\n")
                        continue
            else:
                category_list.append(category)
                break

        while True:
            unit = input("\nEnter the measurement unit used: ").lower()
            if unit == "":
                print("You have not entered any value.\n")
                while True:
                    decision = input("Do you wish to terminate (y/n): ").lower()
                    if decision == "y":
                        code_list.pop(len(code_list) - 1)
                        description_list.pop(len(description_list) - 1)
                        category_list.pop(len(category_list) - 1)
                        return
                    elif decision == "n":
                        break
                    else:
                        print("Invalid input. Please key in again.\n")
                        continue
            else:
                unit_list.append(unit)
                break

        while True:
            price_input = input("\nEnter the item price (RM): ")
            if price_input == "":
                print("You have not entered any value.\n")
                while True:
                    decision = input("Do you wish to terminate (y/n): ").lower()
                    if decision == "y":
                        code_list.pop(len(code_list) - 1)
                        description_list.pop(len(description_list) - 1)
                        category_list.pop(len(category_list) - 1)
                        unit_list.pop(len(unit_list) - 1)
                        return
                    elif decision == "n":
                        break
                    else:
                        print("Invalid input. Please key in again.\n")
                        continue
            else:
                try:
                    price = float(price_input)
                except ValueError:
                    print("The price is invalid. Please provide the correct value.")
                    continue
                else:
                    if float(price) <= 0:
                        print("The price is invalid. Please provide the correct value.")
                        continue
                    else:
                        price_list.append(price)
                        break

        while True:
            quantity_input = input("\nEnter the item quantity: ")
            if quantity_input == "":
                print("You have not entered any value.\n")
                while True:
                    decision = input("Do you wish to terminate (y/n): ").lower()
                    if decision == "y":
                        code_list.pop(len(code_list) - 1)
                        description_list.pop(len(description_list) - 1)
                        category_list.pop(len(category_list) - 1)
                        unit_list.pop(len(unit_list) - 1)
                        price_list.pop(len(price_list) - 1)
                        return
                    elif decision == "n":
                        break
                    else:
                        print("Invalid input. Please key in again.\n")
                        continue
            else:
                try:
                    quantity = int(quantity_input)
                except ValueError:
                    print("The quantity is invalid. Please provide the correct value.")
                    continue
                else:
                    if int(quantity) < 0:
                        print("The quantity is invalid. Please provide the correct value.")
                        continue
                    else:
                        quantity_list.append(quantity)
                        break

        while True:
            threshold_input = input("\nEnter the minimum quantity allowed for the item: ")
            if threshold_input == "":
                print("You have not entered any value.\n")
                while True:
                    decision = input("Do you wish to terminate (y/n): ").lower()
                    if decision == "y":
                        code_list.pop(len(code_list) - 1)
                        description_list.pop(len(description_list) - 1)
                        category_list.pop(len(category_list) - 1)
                        unit_list.pop(len(unit_list) - 1)
                        price_list.pop(len(price_list) - 1)
                        quantity_list.pop(len(quantity_list) - 1)
                        return
                    elif decision == "n":
                        break
                    else:
                        print("Invalid input. Please key in again.\n")
                        continue
            else:
                try:
                    threshold = int(threshold_input)
                except ValueError:
                    print("The input provided is invalid. Please provide the correct value.")
                    continue
                else:
                    if int(threshold) < 0:
                        print("The input provided is invalid. Please provide the correct value.")
                        continue
                    else:
                        threshold_list.append(threshold)
                        break

        print("\nThe current record is saved. All records will be appended to the text file once the program exits.")
        while True:
            decision = input("\nDo you wish to proceed to the next record (y/n): ").lower()
            if decision == "y":
                break
            elif decision == "n":
                return
            else:
                print("This is not a valid answer. Please provide the correct choice.")
                continue


def insert_process():

    """After adding items to empty lists, this function appends the items to inventory.txt"""

    clear_inventory()
    append_file_to_inventory()
    insert_to_list()
    write_inventory_to_file()


def modify_list():

    """This function modifies the items in the lists (for inventory)."""

    append_file_to_inventory()
    file = open("inventory.txt", "r")
    line_list = []
    for line in file.readlines():
        line_list.append(line)
    print("\nWelcome to the interface for updating items.")
    while True:
        code = input("\nEnter the code of the product that you wish to modify: ")
        if code == "":
            print("You did not enter any value.\n")
            while True:
                decision = input("Do you wish to terminate (y/n): ").lower()
                if decision == "y":
                    return
                elif decision == "n":
                    break
                else:
                    print("This is not a valid input. Please try again.\n")
                    continue
        elif code not in code_list:
            print("The code you provided is not in the list. Please key in the correct code.")
            continue
        else:
            print("\nThe involved record is:")
            print(line_list[code_list.index(code)])

            while True:
                print("\nWhich attribute do you wish to modify?"
                      "\n1 - Code"
                      "\n2 - Description"
                      "\n3 - Category"
                      "\n4 - Unit"
                      "\n5 - Price"
                      "\n6 - Minimum quantity")

                choice = input("\nPlease indicate your choice: ")
                if choice == "":
                    print("You did not enter any value.\n")
                    while True:
                        decision = input("Do you wish to terminate (y/n): ").lower()
                        if decision == "y":
                            return
                        elif decision == "n":
                            break
                        else:
                            print("This is not a valid input. Please try again.\n")
                            continue
                else:
                    try:
                        value = int(choice)
                    except ValueError:
                        print("This is not the correct choice. Please choose again.")
                        continue
                    else:
                        if value not in range(1, 7):
                            print("This is not the correct choice. Please choose again.")
                            continue
                        else:
                            while True:
                                new_value = "_".join(input("\nPlease enter your new value: ").title().split())
                                if new_value == "":
                                    print("You did not enter any value.\n")
                                    while True:
                                        decision = input("Do you wish to terminate (y/n): ").lower()
                                        if decision == "y":
                                            return
                                        elif decision == "n":
                                            break
                                        else:
                                            print("This is not a valid input. Please try again.\n")
                                            continue
                                elif value == 1:
                                    if new_value in code_list:
                                        print("The code list is used by another item.\n")
                                        while True:
                                            decision = input("Do you wish to use another code (y/n): ").lower()
                                            if decision == "y":
                                                break
                                            elif decision == "n":
                                                print("You can always come back to this section to modify your record.")
                                                return
                                            else:
                                                print("The input is invalid. Please try again.\n")
                                                continue
                                    else:
                                        code_list[code_list.index(code)] = new_value
                                        code = new_value
                                        break
                                elif value == 2:
                                    if new_value in description_list:
                                        print("This item is already in the list.\n")
                                        while True:
                                            decision = input("Do you wish to use another description (y/n): ").lower()
                                            if decision == "y":
                                                break
                                            elif decision == "n":
                                                print("Please modify the record by using back the assigned code.")
                                                return
                                            else:
                                                print("The input is invalid. Please try again.")
                                                continue
                                    else:
                                        description_list[code_list.index(code)] = new_value
                                        break
                                elif value == 3:
                                    category_list[code_list.index(code)] = new_value.lower()
                                    break
                                elif value == 4:
                                    unit_list[code_list.index(code)] = new_value.lower()
                                    break
                                elif value == 5:
                                    try:
                                        test = float(new_value)
                                    except ValueError:
                                        print("Invalid price. Please try again.")
                                        continue
                                    else:
                                        if test < 0:
                                            print("Invalid price. Please try again.")
                                            continue
                                        price_list[code_list.index(code)] = round(test, 2)
                                        break
                                elif value == 6:
                                    try:
                                        test = int(new_value)
                                    except ValueError:
                                        print("This is not a valid quantity. Please try again.")
                                        continue
                                    else:
                                        if test < 0:
                                            print("This is not a valid quantity. Please try again.")
                                            continue
                                        threshold_list[code_list.index(code)] = test
                                        break

                    while True:
                        choice = input("\nDo you wish to modify other aspects for the same record (y/n): ").lower()
                        if choice == "y":
                            break
                        elif choice == "n":
                            return
                        else:
                            print("The input is invalid. Please try again.")
                            continue


def modify_process():

    """After modifying the items in the lists, this function appends the items in the lists to inventory.txt"""

    clear_inventory()
    modify_list()
    write_inventory_to_file()


def delete_process():

    """This function deletes all related elements from the lists (for inventory), and write to the file."""

    clear_inventory()
    append_file_to_inventory()
    file = open("inventory.txt", "r")
    line_list = []
    for line in file:
        line_list.append(line)
    print("\nWelcome to the interface for removing items.")
    while True:
        code = input("\nProvide the product code that you wish to remove: ")
        if code == "":
            print("You did not enter any value.\n")
            while True:
                decision = input("Do you wish to terminate (y/n): ").lower()
                if decision == "y":
                    return
                elif decision == "n":
                    break
                else:
                    print("This is not a valid input. Please try again.\n")
                    continue
        elif code not in code_list:
            print("The code is not in the record. Please try again.")
            continue
        else:
            print("\nThe record involved is:")
            index_num = code_list.index(code)
            print(line_list[index_num])
            while True:
                decision = input("Do you wish to proceed (y/n): ").lower()
                if decision == "y":
                    line_list.pop(index_num)
                    code_list.pop(index_num)
                    description_list.pop(index_num)
                    category_list.pop(index_num)
                    unit_list.pop(index_num)
                    price_list.pop(index_num)
                    quantity_list.pop(index_num)
                    threshold_list.pop(index_num)
                    print("The record has been deleted.")
                    break
                elif decision == "n":
                    break
                else:
                    print("Invalid input. Please try again.\n")
                    continue

            write_inventory_to_file()

            while True:
                decision = input("\nDo you wish to remove another item (y/n): ").lower()
                if decision == "y":
                    break
                elif decision == "n":
                    return
                else:
                    print("Invalid input. Please try again.\n")
                    continue


def stock_taking():

    """This function is used to change the quantity of items."""

    clear_inventory()
    append_file_to_inventory()
    while True:
        code = input("\nEnter the product code that you wish to modify: ")
        if code == "":
            print("You have entered nothing.\n")
            while True:
                decision = input("Do you wish to terminate (y/n): ").lower()
                if decision == "y":
                    return
                elif decision == "n":
                    print("Please provide a proper code.")
                    break
                else:
                    print("The input is invalid. Please try again.")
                    continue
        elif code not in code_list:
            print("The code is not in the record. Please try again.")
            continue
        else:
            print("\nThe record involved is:")
            file = open("inventory.txt", "r")
            line_list = []
            for line in file:
                line_list.append(line.strip())
            print(line_list[code_list.index(code)])
            while True:
                decision = input("\nDo you wish to proceed (y/n): ").lower()
                if decision == "y":
                    while True:
                        quantity = input("\nInsert the quantity of the item: ")
                        if quantity == "":
                            print("You have entered nothing.\n")
                            while True:
                                decision = input("Do you wish to terminate (y/n): ").lower()
                                if decision == "y":
                                    return
                                elif decision == "n":
                                    print("Please provide a proper quantity.")
                                    break
                                else:
                                    print("The input is invalid. Please try again.")
                                    continue
                        else:
                            try:
                                quantity = int(quantity)
                                if quantity < 0:
                                    print("The quantity is not valid. Please try again.")
                                    continue
                                quantity_list[code_list.index(code)] = quantity
                                break
                            except ValueError:
                                print("The quantity is not valid. Please try again.")
                                continue
                    break

                elif decision == "n":
                    break
                else:
                    print("Invalid input. Please try again.")
                    continue

            write_inventory_to_file()

            while True:
                decision = input("\nDo you wish to move on to the next record (y/n): ").lower()
                if decision == "y":
                    break
                elif decision == "n":
                    return
                else:
                    print("Invalid input. Please try again.")
                    continue


def view_replenish():

    """This function compares the quantity and the threshold to identify the items needed to be replenished."""

    clear_inventory()
    append_file_to_inventory()
    file = open("inventory.txt", "r")
    line_list = []
    for line in file:
        line_list.append(line.strip())
    temp_list = []
    for num in range(len(code_list)):
        if quantity_list[num] < threshold_list[num]:
            temp_list.append(num)
    if len(temp_list) == 0:
        print("\nThere is no items that need to be replenished.")
    else:
        print("\nThese are the items that has to be replenished:")
        for num in temp_list:
            print(line_list[num])


def stock_replenish():

    """This function adds the entered value to the item quantity."""

    clear_inventory()
    append_file_to_inventory()
    while True:
        code = input("\nEnter the code of product that you have purchased: ")
        if code == "":
            print("You have entered nothing.\n")
            while True:
                decision = input("Do you wish to terminate (y/n): ").lower()
                if decision == "y":
                    return
                elif decision == "n":
                    print("Please provide a proper code.")
                    break
                else:
                    print("The input is invalid. Please try again.\n")
                    continue
        elif code not in code_list:
            print("The code is not recorded. Please try again.")
            continue
        else:
            print("\nThe record involved is:")
            file = open("inventory.txt", "r")
            line_list = []
            for line in file:
                line_list.append(line.strip())
            print(line_list[code_list.index(code)])
            while True:
                decision = input("\nDo you wish to proceed (y/n): ").lower()
                if decision == "y":
                    while True:
                        quantity = input("\nInsert the amount of item that you have purchased: ")
                        if quantity == "":
                            print("You did not insert any values.\n")
                            while True:
                                decision = input("Do you wish to terminate (y/n): ").lower()
                                if decision == "y":
                                    return
                                elif decision == "n":
                                    break
                                else:
                                    print("Invalid input. Please try again.\n")
                                    continue
                        else:
                            try:
                                quantity = int(quantity)
                                if quantity < 0:
                                    print("The quantity is invalid. Please try again.")
                                    continue
                                quantity_list[code_list.index(code)] += quantity
                                break
                            except ValueError:
                                print("The quantity is invalid. Please try again.")
                                continue
                    break
                elif decision == "n":
                    break
                else:
                    print("Invalid input. Please try again.")
                    continue

            write_inventory_to_file()

            while True:
                decision = input("\nDo you wish to move on to the next record (y/n): ").lower()
                if decision == "y":
                    break
                elif decision == "n":
                    return
                else:
                    print("Invalid input. Please try again.")
                    continue


def description_search():

    """This function allows users to search for records using description / item name."""

    clear_inventory()
    append_file_to_inventory()
    file = open("inventory.txt", "r")
    line_list = []
    for line in file:
        line_list.append(line.strip())
    while True:
        search = "_".join(input("\nProvide a description: ").lower().split())
        if search == "":
            print("You did not provide any input.\n")
            while True:
                decision = input("Do you wish to terminate (y/n): ").lower()
                if decision == "y":
                    return
                elif decision == "n":
                    print("Please provide a proper description.")
                    break
                else:
                    print("The input is invalid. Please try again.\n")
                    continue
        else:
            temp_list = []
            for word in description_list:
                if search in word.lower():
                    temp_list.append(line_list[description_list.index(word)])
            if len(temp_list) == 0:
                print("\nNo matching records.")
            else:
                print("\nThe records are:")
                for line in temp_list:
                    print(line)
            return


def code_range_search():

    """This function allows users to search for records based on the given code range"""

    clear_inventory()
    append_file_to_inventory()
    file = open("inventory.txt", "r")
    line_list = []
    for line in file:
        line_list.append(line.strip())
    while True:
        min_range = input("\nPlease provide the minimum for the code range: ")
        max_range = input("Please provide the maximum for the code range: ")
        if min_range == "" or max_range == "":
            print("You did not provide any input.\n")
            while True:
                decision = input("Do you wish to terminate (y/n): ").lower()
                if decision == "y":
                    return
                elif decision == "n":
                    print("Please provide a proper code.")
                    break
                else:
                    print("The input is invalid. Please try again.\n")
                    continue
        else:
            try:
                min_range = int(min_range)
                max_range = int(max_range)
            except ValueError:
                print("The code is invalid. Please try again.")
                continue
            else:
                if min_range < 0 or max_range < 0:
                    print("The code is invalid. Please try again.")
                    continue
                elif min_range > max_range:
                    temp_var = min_range
                    min_range = max_range
                    max_range = temp_var
                temp_list = []
                for code in code_list:
                    if min_range <= int(code) <= max_range:
                        temp_list.append(line_list[code_list.index(code)])
                if len(temp_list) == 0:
                    print("\nNo matching records found.")
                else:
                    print("\nThe records are:")
                    for line in temp_list:
                        print(line)
                return


def category_search():

    """This function allows users to search for items based on category."""

    clear_inventory()
    append_file_to_inventory()
    file = open("inventory.txt", "r")
    line_list = []
    for line in file:
        line_list.append(line.strip())
    while True:
        search = "_".join(input("\nProvide a category: ").lower().split())
        if search == "":
            print("You did not provide any input.\n")
            while True:
                decision = input("Do you wish to terminate (y/n): ").lower()
                if decision == "y":
                    return
                elif decision == "n":
                    print("Please provide a proper category.")
                    break
                else:
                    print("The input is invalid. Please try again.\n")
                    continue
        else:
            temp_list = []
            for num in range(len(code_list)):
                if search in category_list[num]:
                    temp_list.append(line_list[num])
            if len(temp_list) == 0:
                print("\nNo matching records found.")
            else:
                print("\nThe records are:")
                for line in temp_list:
                    print(line)
            return


def price_range_search():

    """This function allows users to search for items based on a price range."""

    clear_inventory()
    append_file_to_inventory()
    file = open("inventory.txt", "r")
    line_list = []
    for line in file:
        line_list.append(line.strip())
    temp_list = []
    while True:
        min_range = input("\nPlease provide the minimum for the price range: ")
        max_range = input("Please provide the maximum for the price range: ")
        if min_range == "" or max_range == "":
            print("You did not provide any input.\n")
            while True:
                decision = input("Do you wish to terminate (y/n): ").lower()
                if decision == "y":
                    return
                elif decision == "n":
                    print("Please provide a proper input.")
                    break
                else:
                    print("The input is invalid. Please try again.\n")
                    continue
        else:
            try:
                min_range = float(min_range)
                max_range = float(max_range)
            except ValueError:
                print("Please provide a proper price.")
                continue
            else:
                if min_range < 0 or max_range < 0:
                    print("Please provide a proper price.")
                    continue
                elif min_range > max_range:
                    temp_var = min_range
                    min_range = max_range
                    max_range = temp_var
                for num in range(len(price_list)):
                    if min_range <= price_list[num] <= max_range:
                        temp_list.append(line_list[num])
                if len(temp_list) == 0:
                    print("\nNo matching records found.")
                else:
                    print("\nThe records are:")
                    for line in temp_list:
                        print(line)
                return


def search_item():

    """This function compiles all the available types of search into one."""

    while True:
        print("\nHow would you like to search for an item?"
              "\n1 - Search by description"
              "\n2 - Search by code range"
              "\n3 - Search by category"
              "\n4 - Search by price range")
        choice = input("\nPlease enter your choice: ")
        if choice == "":
            print("You did not provide any input.")
            while True:
                decision = input("\nDo you wish to terminate (y/n): ").lower()
                if decision == "y":
                    return
                elif decision == "n":
                    break
                else:
                    print("Invalid input. Please try again.")
                    continue
        else:
            try:
                choice = int(choice)
            except ValueError:
                print("Please choose the correct choice.")
                continue
            else:
                if choice not in range(1, 5):
                    print("Please choose the correct choice.")
                    continue
                else:
                    if choice == 1:
                        description_search()
                    elif choice == 2:
                        code_range_search()
                    elif choice == 3:
                        category_search()
                    elif choice == 4:
                        price_range_search()

                    while True:
                        decision = input("\nDo you wish to search for another item (y/n): ").lower()
                        if decision == "y":
                            break
                        elif decision == "n":
                            return
                        else:
                            print("Invalid input. Please try again.")
                            continue


def add_user_to_list():

    """This function adds new users to lists (for users)."""

    while True:
        print("\nPlease provide the necessary details for the new user."
              "\nNote: A username should contain only a word and between 2 to 20 characters. "
              "Usernames are not case-sensitive.")
        while True:
            user = input("\nPlease provide a username: ").lower()
            if user == "":
                print("You did not insert any values.\n")
                while True:
                    decision = input("Do you wish to terminate (y/n): ").lower()
                    if decision == "y":
                        return
                    elif decision == "n":
                        break
                    else:
                        print("Invalid input. Please try again.\n")
                        continue
                continue

            elif (len(user.split()) > 1) or (len(user) > 20) or (len(user) < 2):
                print("The username does not fulfil the requirements. Please try again.")
                continue

            elif user in user_list:
                print("The username has been used. Please choose another username.")
                continue

            else:
                user_list.append(user)
                break

        print("\nNote: Password must contain between 4 to 18 characters. Passwords are case-sensitive.")
        while True:
            password = input("\nPlease provide a password: ")
            if password == "":
                print("You did not insert any values.\n")
                while True:
                    decision = input("Do you wish to terminate (y/n): ").lower()
                    if decision == "y":
                        user_list.pop(-1)
                        return
                    elif decision == "n":
                        break
                    else:
                        print("Invalid input. Please try again.\n")
                        continue
                continue
            elif len(password) < 4 or len(password) > 18:
                print("The password does not fulfil the requirements.")
                continue
            else:
                password_list.append(password)
                break

        print("\nThe available user types are:"
              "\n1 - Admin"
              "\n2 - Inventory checker"
              "\n3 - Purchaser")
        while True:
            usertype = input("\nPlease indicate your choice: ")
            if usertype == "":
                print("You did not insert any values.\n")
                while True:
                    decision = input("Do you wish to terminate (y/n): ").lower()
                    if decision == "y":
                        user_list.pop(-1)
                        password_list.pop(-1)
                        return
                    elif decision == "n":
                        break
                    else:
                        print("Invalid input. Please try again.\n")
                        continue
                continue
            try:
                usertype = int(usertype)
            except ValueError:
                print("Invalid input. Please try again.")
                continue
            else:
                if usertype not in [1, 2, 3]:
                    print("Invalid input. Please try again.")
                    continue
                else:
                    if usertype == 1:
                        usertype_list.append("Admin")
                    elif usertype == 2:
                        usertype_list.append("Inventory_checker")
                    else:
                        usertype_list.append("Purchaser")
                    print("New user saved successfully.")
                    break

        while True:
            decision = input("\nDo you wish to insert another user (y/n): ").lower()
            if decision == "y":
                break
            elif decision == "n":
                return
            else:
                print("Invalid input. Please try again.")
                continue
        continue


def add_new_user():

    """After adding new users to the lists, this function adds the users to username.txt"""

    clear_user()
    append_file_to_user()
    add_user_to_list()
    write_user_to_file()


def user_authentication():

    """This is the main function that controls the login module."""

    append_file_to_user()
    print("\nWelcome to Happy Day Grocery Store Inventory System.")
    print("Please sign in to proceed.")
    while True:
        username = input("\nPlease provide your username: ").lower()
        if username == "":
            print("You did not provide any input.\n")
            while True:
                decision = input("Do you wish to exit (y/n): ").lower()
                if decision == "y":
                    print("\nThank you for using the system!")
                    exit()
                elif decision == "n":
                    break
                else:
                    print("Invalid input. Please try again.\n")
                    continue
            continue
        else:
            password = input("Please provide your password: ")
            try:
                if password == password_list[user_list.index(username)]:
                    user_type = usertype_list[user_list.index(username)]
                    print("\nLogin successful.")
                    print("Note: Hit 'Enter' with nothing to terminate actions.\n")
                    while True:
                        if user_type == "Admin":
                            print("The available actions are:"
                                  "\n1 - Add new user"
                                  "\n2 - Insert new item"
                                  "\n3 - Update item"
                                  "\n4 - Delete item"
                                  "\n5 - Stock-taking"
                                  "\n6 - View replenish list"
                                  "\n7 - Stock replenishment"
                                  "\n8 - Search items"
                                  "\n9 - Change user details")
                            while True:
                                choice = input("\nPlease provide a choice: ")
                                if choice == "1":
                                    add_new_user()
                                    break
                                elif choice == "2":
                                    insert_process()
                                    break
                                elif choice == "3":
                                    modify_process()
                                    break
                                elif choice == "4":
                                    delete_process()
                                    break
                                elif choice == "5":
                                    stock_taking()
                                    break
                                elif choice == "6":
                                    view_replenish()
                                    break
                                elif choice == "7":
                                    stock_replenish()
                                    break
                                elif choice == "8":
                                    search_item()
                                    break
                                elif choice == "9":
                                    change_user_details()
                                    break
                                elif choice == "":
                                    print("You did not provide any input.\n")
                                    while True:
                                        decision = input("Do you wish to terminate (y/n): ").lower()
                                        if decision == "y":
                                            print("\nThank you for using the system!")
                                            exit()
                                        elif decision == "n":
                                            break
                                        else:
                                            print("Invalid input. Please try again.\n")
                                            continue
                                else:
                                    print("Invalid input. Please try again.")
                                    continue

                        elif user_type == "Inventory_checker":
                            print("The available actions are:"
                                  "\n1 - Stock-taking"
                                  "\n2 - Search items")
                            while True:
                                choice = input("\nPlease provide a choice: ")
                                if choice == "1":
                                    stock_taking()
                                    break
                                elif choice == "2":
                                    search_item()
                                    break
                                elif choice == "":
                                    print("You did not provide any input.")
                                    while True:
                                        decision = input("\nDo you wish to terminate (y/n): ").lower()
                                        if decision == "y":
                                            print("\nThank you for using the system!")
                                            exit()
                                        elif decision == "n":
                                            break
                                        else:
                                            print("Invalid input. Please try again.")
                                            continue
                                else:
                                    print("Invalid input. Please try again.")
                                    continue

                        else:
                            print("The available actions are:"
                                  "\n1 - View replenish list"
                                  "\n2 - Stock replenishment"
                                  "\n3 - Search items")
                            while True:
                                choice = input("\nPlease provide a choice: ")
                                if choice == "1":
                                    view_replenish()
                                    break
                                elif choice == "2":
                                    stock_replenish()
                                    break
                                elif choice == "3":
                                    search_item()
                                    break
                                elif choice == "":
                                    print("You did not provide any input.\n")
                                    while True:
                                        decision = input("Do you wish to terminate (y/n): ").lower()
                                        if decision == "y":
                                            print("\nThank you for using the system!")
                                            exit()
                                        elif decision == "n":
                                            break
                                        else:
                                            print("Invalid input. Please try again.\n")
                                            continue
                                else:
                                    print("Invalid input. Please try again.")
                                    continue

                        while True:
                            decision = input("\nDo you wish to go back to the main menu (y/n): ").lower()
                            if decision == "y":
                                print("")
                                break
                            elif decision == "n":
                                print("\nThank you for using the system!")
                                exit()
                            else:
                                print("\nInvalid input. Please try again.")
                                continue
                else:
                    print("Incorrect username or password.\n")
                    while True:
                        decision = input("Do you wish to try again (y/n): ").lower()
                        if decision == "y":
                            break
                        elif decision == "n":
                            print("\nThank you for using the system!")
                            exit()
                        else:
                            print("Invalid input. Please try again.\n")
                            continue

            except ValueError:
                print("\nIncorrect username or password.")
                while True:
                    decision = input("Do you wish to try again (y/n): ").lower()
                    if decision == "y":
                        break
                    elif decision == "n":
                        print("\nThank you for using the system!")
                        exit()
                    else:
                        print("Invalid input. Please try again.\n")
                        continue


def modify_user():

    clear_user()
    append_file_to_user()
    temp_list = []
    for position in range(len(user_list)):
        temp_list.append(f'{user_list[position]:25}'
                         f'{password_list[position]:25}'
                         f'{usertype_list[position]:20}\n')

    print("\nWelcome to the interface for modifying user details.")
    while True:
        username_input = input("\nPlease provide the username that you wish to modify: ").lower()
        if username_input == "":
            print("You did not provide any input.\n")
            while True:
                decision = input("Do you wish to exit (y/n): ").lower()
                if decision == "y":
                    return
                elif decision == "n":
                    break
                else:
                    print("Invalid input. Please try again.")
                    continue
        elif username_input not in user_list:
            print("The user is not available.")
            while True:
                decision = input("\nDo you wish to try again (y/n): ").lower()
                if decision == "y":
                    break
                elif decision == "n":
                    return
                else:
                    print("Invalid input. Please try again.")
                    continue
        else:
            print("\nThe user involved is: ")
            print(temp_list[user_list.index(username_input)])
            while True:
                decision = input("Do you wish to continue (y/n): ").lower()
                if decision == "y":
                    print("\nHere are the aspects that you can change:")
                    print("1 - Password")
                    print("2 - User type")
                    while True:
                        choice = input("\nPlease enter your choice: ")
                        if choice == "":
                            print("You did not provide any input.\n")
                            while True:
                                decision = input("Do you wish to exit (y/n): ").lower()
                                if decision == "y":
                                    return
                                elif decision == "n":
                                    break
                                else:
                                    print("Invalid input. Please try again.\n")
                                    continue
                        elif choice == "1":
                            print("\nNote: Password must contain between 4 to 18 characters. "
                                  "Passwords are case-sensitive.")
                            while True:
                                password = input("\nPlease provide a new password: ")
                                if password == "":
                                    print("You did not insert any values.\n")
                                    while True:
                                        decision = input("Do you wish to terminate (y/n): ").lower()
                                        if decision == "y":
                                            return
                                        elif decision == "n":
                                            break
                                        else:
                                            print("Invalid input. Please try again.\n")
                                            continue
                                elif len(password) < 4 or len(password) > 18:
                                    print("The password does not fulfil the requirements.")
                                    continue
                                else:
                                    password_list[user_list.index(username_input)] = password
                                    print("The password has been changed.")
                                    return
                        elif choice == "2":
                            print("\nThere are three user types:")
                            print("1 - Admin")
                            print("2 - Inventory checker")
                            print("3 - Purchaser")
                            while True:
                                decision = input("\nPlease provide your choice: ")
                                if decision == "":
                                    print("You did not insert any values.\n")
                                    while True:
                                        decision = input("Do you wish to terminate (y/n): ").lower()
                                        if decision == "y":
                                            return
                                        elif decision == "n":
                                            break
                                        else:
                                            print("Invalid input. Please try again.\n")
                                            continue
                                elif decision == "1":
                                    usertype_list[user_list.index(username_input)] = "Admin"
                                    print("Successfully changed to 'Admin'.")
                                    return
                                elif decision == "2":
                                    usertype_list[user_list.index(username_input)] = "Inventory_checker"
                                    print("Successfully changed to 'Inventory checker'.")
                                    return
                                elif decision == "3":
                                    usertype_list[user_list.index(username_input)] = "Purchaser"
                                    print("Successfully changed to 'Purchaser'.")
                                    return
                                else:
                                    print("Invalid input. Please provide the correct choice.")
                                    continue
                        else:
                            print("Invalid input. Please provide the correct choice.")
                            continue
                elif decision == "n":
                    while True:
                        choice = input("\nDo you wish to modify another user (y/n): ").lower()
                        if choice == "y":
                            break
                        elif choice == "n":
                            return
                        else:
                            print("Invalid input. Please try again.")
                            continue
                    break
                else:
                    print("Invalid input. Please try again.\n")
                    continue


def change_user_details():

    modify_user()
    write_user_to_file()


# Empty lists related to inventory
code_list = []
description_list = []
category_list = []
unit_list = []
price_list = []
quantity_list = []
threshold_list = []

# Empty lists related to users (login module).
user_list = []
password_list = []
usertype_list = []


# Run the login module and start the program.
user_authentication()
