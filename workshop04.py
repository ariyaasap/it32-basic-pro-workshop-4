gang_member = []
def add_member(name,age,gang):
    new_member = {'name':name,'age':age,'gang':gang}
    gang_member.append(new_member)


while True:
    choice = str(input(" 1 for Add member | 2 for Show member | [Any Key] Quite: "))
    if choice == "1" :
        name = input('Emter your name: ')
        age = input('Emter your age: ')
        gang = input('Emter your gang: ')
        add_member(name,age,gang)
    
    elif choice == "2" :
        print(gang_member)
    else:
        print("quit")
        break


