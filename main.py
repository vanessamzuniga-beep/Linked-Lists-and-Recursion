from linked_list import LinkedList

if __name__ == "__main__":
    """
    Use this file to create a LinkedList instance and perform operations 
    like insertion, recursion-based sum, search, and reverse.
    """

    # TODO: 1) Create a LinkedList instance
    linked_list = LinkedList()
    

    # TODO: 2) Insert some sample data using insert_at_front or insert_at_end
    linked_list.insert_at_end(10)
    linked_list.insert_at_end(20)
    linked_list.insert_at_end(30)
    linked_list.insert_at_end(40)
    
    # TODO: 3) Display the list to verify insertion
    print("Original list:")
    linked_list.display()
    

    # TODO: 4) Call recursive_sum and print the result
    print("Sum:", linked_list.recursive_sum())
    

    # TODO: 5) Call recursive_search with a target and print result
    print("Search for 30:", linked_list.recursive_search(30))
    

    # TODO: 6) Call recursive_reverse, then display the reversed list
    print("Reversed list:")
    linked_list.recursive_reverse()
    linked_list.display()






    

    


    


# 