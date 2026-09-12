# # Store contacts as a list of dictionaries: {"name": ..., "phone": ...}
# # Three functions:
# # add_contact(contacts, name, phone) — adds a new contact dict to the list
# # search_contact(contacts, name) — finds and returns the contact(s) matching that name
# # list_contacts(contacts) — returns/prints all contacts


contacts=[]

def add_contact():
    new_contact={}
    name=input("Enter name: ")
    new_contact['name']=name
    phone=int(input("Enter phone No: "))
    new_contact['phone']=phone

    contacts.append(new_contact)

def search_contact(contacts,name):
    found=False
    for contact in contacts:
        
        if contact['name']==name:
            found=True
            print( "CONTACT NO: ",contact['name'],"PHONE NO: ", contact['phone'])
    if not found:        
        print("No contact Found")    

def list_contact(contacts): 
    for contact in contacts:
        print (contact)               
 
print("----CONTACT BOOK----")
while True:
    option=input("choose function to perform \n 1)add contact \n 2)search contact \n 3)list contact \n 4)exit  ")

    if option=="1":
        add_contact()
    elif option=="2":
        user_name=input("Enter Name: ") 
        search_contact(contacts,user_name)
    elif option=="3":
        list_contact(contacts)
    elif option=="4":
        break    

    else:
        print("Invalid")    

# CHALLENGE
# Write a function clean_contact_list(contacts: list) -> list that removes duplicate contacts (same phone
# number) and returns a cleaned list, keeping the first occurrence

def clean_contact_list(contacts):
    clean_list=[]
    seen_phones=[]
    for contact in contacts:
        if contact['phone'] not in seen_phones:
           clean_list.append(contact)
           seen_phones.append(contact['phone'])
            

    return(clean_list) 
contacts=[
    {'name': 'uk', 'phone': 875767},
    {'name': 'zara', 'phone': 767567},
    {'name': 'irha', 'phone': 656568},
    {'name': 'uk home', 'phone': 875767},
    {'name': 'zara nasir', 'phone': 767567},]

print(clean_contact_list(contacts))       

