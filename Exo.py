todos = []
def create_todo():
    todo = (input("enter todo name : "),"To do")
    if todo not in todos: 
        todos.append(todo)
    else :
        print("this To do already exists ! ")
        
def lister_todos() : 
    print("")
    for i in range (len(todos)) : 
        print (f"{i + 1} = {todos[i][0]} ({todos[i][1]})")
    if not todos : 
        print ("you don't have any to do yet ! ")
        
def modify_status_todos() :
    print ("enter the todos number that you want to modify : ")
    choice = input("choice :")
    print ("")
    if choice.isnumeric() : 
        choice = int(choice)
        if 1 <= choice <= len(todos):
            current_todo = todos[choice - 1]
            if current_todo[1] == "To do":
                todos[choice - 1] = (current_todo[0], "Done")
            else:
                todos[choice - 1] = (current_todo[0], "To do")
            print(f"The status of '{current_todo[0]}' has been updated!")
        else:
            print("This todo doesn't exist!")
    else:
        print("Please try again by entering a valid number!")

def delete_todo():
    lister_todos() 
    print("")
    print ("enter the todos number that you want to modify : ")
    choice = input("choice : ")
    print ("")
    if choice.isnumeric() : 
        choice = int(choice)
        if choice <= len(todos) : 
            if todos[choice -1] : 
                if input ("Do you really want to delete this To-do ? (o/n) : ") == "o" :
                    del todos[choice - 1]
                    print("todo deleted !")
        else : 
            print ("This to_do doesn't exist ! ")
    else :
        print("please try again by entering a number !")
        delete_todo()
def main():
    while True:
        print("\n--- Todo Manager ---")
        print("1. Add a new todo")
        print("2. List all todos")
        print("3. Modify todo status")
        print("4. Delete a todo")  # Option ajoutée
        print("5. Quit")  # Mise à jour du numéro de l'option Quit
        choice = input("Enter your choice: ")

        if choice == "1":
            create_todo()
        elif choice == "2":
            lister_todos()
        elif choice == "3":
            modify_status_todos()
        elif choice == "4":  # Ajout de l'appel à delete_todo
            delete_todo()
        elif choice == "5":  # Numéro mis à jour pour Quit
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again!")

# Lancer le programme
if __name__ == "__main__":
    main()
    choice = input("choice : ")
    print ("")
    if choice.isnumeric() : 
        choice = int(choice)
        if choice <= len(todos) : 
            if todos[choice -1] : 
                if input ("Do you really want to delete this To-do ? (o/n) : ") == "o" :
                    del todos[choice - 1]
                    print("todo deleted !")
        else : 
            print ("This to_do doesn't exist ! ")
    else :
        print("please try again by entering a number !")
