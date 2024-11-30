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
        if choice <= len(todos) : 
            if todos [choice - 1][1] == "do" :
                todos [choice - 1][1] == "to do"
            elif not todos [choice - 1][1] == "to do" :
                todos [choice - 1][1] == "do" 
        else : 
            print ("This to do doesn't exist !")
    else : 
        print("please try again by entering a number !")
        modify_status_todos()
        
        
                    