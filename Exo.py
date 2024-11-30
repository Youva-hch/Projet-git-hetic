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
        