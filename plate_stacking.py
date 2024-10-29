

class Node:
    """
    A class used to represent a Node in a stack.

    Attributes
    ----------
    value : int
        The value stored in the node.
    next : Node
        The next node in the stack.
    """
     
    def __init__(self, value):
        """
        Parameters
        ----------
        value : int
            The value to be stored in the node.
        """
        self.value = value
        self.next = None
        
class Stack:
    """
    A class used to represent the Stack (The plate "below" is greater or equal to the "top")
    Attributes
    ----------
    top : Node
        The top node of the stack.
    height : int
        The number of nodes in the stack.
    """
    def __init__(self, value):
        """
        Parameters
        ----------
        value : int
            The initial value for the stack. Must be greater than 0.
        """
       
        while value <= 0:
            print("Enter plate number greater than 0")
            value = int(input("Enter value to start the stack: "))
        new_node = Node(value)
        self.top = new_node
        self.height = 1
       
    def print_stack(self):
        """
        Prints the values in the stack from top to bottom.
        """

        temp = self.top
        if temp is None:
            print("Stack is empty")
        while temp is not None:
            print(temp.value)
            temp = temp.next
            

    def add_stack(self, value):
        """
        Adds a new node with the given value to the stack.

        Parameters
        ----------
        value : int
            The value to be added to the stack. Must be greater than 0.
        """
        if value <= 0:
            print("Value must be greater than 0")
            return
        new_node = Node(value)
        if value < self.top.value:
            new_node.next = self.top
            self.top = new_node
        
        else:
            temp = self.top
            while temp.next is not None and temp.next.value < value:
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node

            #self.top = new_node
        self.height += 1
    
    def delete_stack(self):
        """
        Removes the node with the specified value from the stack.

        Returns
        -------
        Node or None
            The removed node if found, otherwise None.
        """
        if self.height == 0:
            print("Stack is empty")
            return None
        
        pop_input = int(input("Input plate number to delete: "))
        temp = self.top
        prev = None
        while temp is not None:
            if temp.value == pop_input:
                if prev is None:
                    self.top = temp.next
                else:
                    prev.next = temp.next
                temp.next = None
                self.height -= 1
                return temp
            prev = temp
            temp = temp.next
        print(f"Value {pop_input} not found in the stack")
        return None

    
value = int(input("Insert initial value for the stack: "))
my_stack = Stack(value)

while True:
    cli_action = int(input(
        "Enter action:\n"
        "1: Print Plates\n"
        "2: Add a Plate\n"
        "3: Remove Plates\n"
        "4: exit\n"
        "Select [1-4]: "
    ))
    try:
        cli_action = int(cli_action)
    except ValueError:
        print("Invalid cli action. Please enter a number.")
        continue
    print("---------------------------------------------")
    match cli_action:
        case 1:
            print("Current Stack: ")
            my_stack.print_stack()
        case 2:
            print("Current Stack: ") 
            value = int(input("Insert value to push: "))
            my_stack.add_stack(value)
        case 3:
            print("Current Stack: ")
            my_stack.print_stack()
            my_stack.delete_stack()
        case 4:
            print("Thank you for using this program!")
            break
        case _:
            print("Invalid cli action. Please try again.")
   
    print("---------------------------------------------")
