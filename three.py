def choose_three(text, optionA, optionB, optionC):
    print(text)
    print("A. ", optionA)
    print("B. ", optionB)
    print("C. ", optionC)
    
    while True:
        choice = input("Choose A, B, or C: ").upper()
        if choice == 'A' or choice == 'B' or choice == 'C':
            return choice
        else:
            print("Invalid option, try again.")
