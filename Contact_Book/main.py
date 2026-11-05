print("\nContacts Book")
print("1.Add Contact")
print("2.View all Contacts")
print("3.Search Contact")
print("4.Update Contact")
print("5.Delete Contact")


def main():
    while True:
        try:
           choice = int(input("Enter Your Choice: "))
           if choice == 1:
            add_contact()

           elif choice == 2:
            view_all_contacts()

           elif choice == 3:
            search_contact()

           elif choice == 4:
            update_contact()

           elif choice == 5:
            delete_contact()
            break
           else:
            print("Enter Correct Choice.")

        except ValueError:
           print("Enter Valid input.")

contacts = {}

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    email = input("Enter Email: ")
    city = input("Enter City: ")

    contacts[name] = {"phone":phone,"email":email,"city":city}

    print("Contact Added Successfuly.")

def view_all_contacts():
    print("View All Contacts:")
    if len(contacts) ==0:
        print("No one contact in book.")
    else:
     for name,details in contacts.items():
        if len(contacts) == 0:
           print("No contact in Dictionory")
        else:
           print("Name:",name)
           print("Phone:",details["phone"])
           print("Email:",details["email"])
           print("City:",details["city"])

def search_contact():
        name = input("Enter Contact Name: ")
        details = contacts[name]
        
    # for name ,details in contacts.items():
        
        if name in contacts:
            print("Name:",name)
            print("Phone:",details["phone"])
            print("Email:",details["email"])
            print("City:",details["city"])

        else:
            print("Contact Not Found.")

def update_contact():
    if len(contacts) == 0:
        print("No Contact Available.")

    else:
        name = input("Enter Contact Name:")
        if name in contacts:
            print("\nWhat do you want update?")
            print("1.Phone")
            print("2.Email")
            print("3.City")
            print("4.No One")
            try:
                choice = int(input("Enter Your Choice: "))
                if choice ==1:
                    new_phone = input("Enter New Phone: ")
                    contacts[name]["phone"] = new_phone
                    print("Phone Updated Successfuly.")

                elif choice == 2:
                    new_email = input("Enter New Email: ")
                    contacts[name]["email"] = new_email
                    print("Email updated Successfuly.")

                elif choice == 3:
                    new_city = input("Enter New City: ")
                    contacts[name]["city"] = new_city
                    print("City Updated successfuly.")

                elif choice == 4:
                    print("No Update.")
                

                else:
                    print("Invalid Choice.")

                    
                
            except ValueError:
                print("Enter valid Number.")

        else:
            print("Contact Not found.")

def delete_contact():
    if len(contacts) ==0:
        print("No Contact Available.")

    else:
        name = input("Enter Contact Name: ")
        if name in contacts:
            contacts.pop(name)  
            print("Contact Delete Successfuly")

        else:
            print("Contact Not Found.")   
                    
main()
# add_contact()
# view_all_contacts()   
# search_contact()
# update_contact()
# delete_contact()
