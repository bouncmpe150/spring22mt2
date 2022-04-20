members = ['Veronica Pittman', 'Heena Hooper', 'Uma Davidson', 'Amit Cook', 'Malik Clifford', 'Griffin Abbott', 'Aiysha Villa',
           'Stacie Kane', 'Arandeep Conway', 'Harrison Cameron', 'Shayna John', 'Gia Odonnell', 'Katarina Mcmanus', 'Toni Mellor', 
           'Rogan Floyd', 'Anum Lake', 'Elora Mcbride', 'Aariz Shea', 'Gaia Wooten', 'Frederick Bonilla', 'Anastazja Bonner', 
           'Ellie Obrien', "Carmel O'Brien", 'Elsie Blanchard', 'Rukhsar Houston', 'Aanya Akhtar', 'Vicky Livingston', 'Tarik Gentry', 
           'Amber-Rose Lam', 'Ryan Dixon', 'Finnian Perkins', 'Eiliyah Bowes', 'Joyce Bright', 'Renzo Ewing', 'Yusra Mcpherson', 
           'Sallie Maynard', 'Abdullah Ritter', 'Nabil Hook', 'Emer Beattie', 'Aiesha Mcdougall', 'Anya Black', 'Tony Mustafa', 
           'Mitchell Hayward', 'Walid Butler', 'Samir Huber', 'Gordon Hassan', 'Leanna Olsen', 'Branden Whitley', 'Sasha Parry', 
           'Una Allan', 'Lucie Southern', 'Nia Cabrera', 'Chante Sloan', 'Stewart Grey', 'Dillan Phan', 'Francesco Hollis', 
           'April Neal', 'Kwabena House', 'Jadon Cordova', 'Brooke Robinson', 'Gary Davila', 'Uwais Naylor', 'Shirley Ahmad', 
           'Om Carney', 'Nazim Owens', 'Elissa Hewitt', 'Mabel Croft', 'Hamza Knapp', 'Micheal Crosby', 'Karter Hines', 
           'Ann Faulkner', 'Lochlan Wainwright', 'Olivia-Grace Robbins', 'Mahek Dominguez', 'Anja Spence', 'Bella Reese', 
           'Samiha Dodd', 'Taryn Correa', 'Dylon Arellano', 'Conal Fischer', 'June Rowe', 'Arwen Mays', 'Adelle Vargas', 
           'Annie Johnson', 'Jimi Leach', 'Zachary Harwood', 'Tiernan Ellwood', 'Coen Keenan', 'Jody Horner', 'Xena Howell', 
           'Avni Quinn', 'Monica Tillman', 'Muskaan Reyes', 'Saara Goodman', 'Bob Hebert', 'Aras Cooper', 'Duane Adam', 
           'Cecil Corona', 'Esha Felix', 'Mayur Steele']
unreturned_books = [4, 2, 3, 2, 4, 3, 3, 2, 3, 2, 4, 0, 4, 4, 3, 1, 0, 0, 0, 3, 4, 2,
       2, 3, 3, 0, 0, 2, 4, 4, 4, 2, 3, 3, 4, 0, 2, 3, 3, 0, 2, 1, 4, 1,
       2, 3, 1, 3, 0, 2, 1, 1, 0, 3, 1, 3, 1, 0, 1, 2, 1, 4, 2, 2, 0, 3,
       1, 1, 4, 3, 1, 3, 4, 0, 0, 3, 1, 3, 3, 0, 2, 1, 2, 1, 3, 3, 0, 4,
       0, 2, 4, 3, 1, 1, 4, 1, 2, 2, 2, 2]
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
finished = False # the user can at most have 5 unreturned books and can borrow at most 3 books at the same time, check if they are returning more books than they borrowed

while not finished:
    operation = input() # 'borrow' or 'return' or 'exit'
    while operation not in ['borrow', 'return', 'exit']:
        operation = input()
        
    if operation == 'exit':
        finished = True
        break
        
    user_id = input()
    while user_id not in members:
        user_id = input()

    amount = int(input())
    while amount <= 0:
        amount = int(input())

    i = members.index(user_id)
    user_account_info = unreturned_books[i]

    if operation == "borrow" and amount > 3:
        print("You cannot borrow more than 3 books at the same time")
        continue
    
    elif operation == "borrow" and (user_account_info == 5 or (user_account_info + amount > 5)):
        print("You must return the books you borrowed first")
        continue
        
    elif user_account_info < amount and operation == "borrow":
        old_amount = unreturned_books[i]
        unreturned_books[i] += amount
        print(old_amount, "=>", unreturned_books[i])
        continue
    
    elif operation == 'return' and amount > user_account_info:
        print("Whose books are they?")
        continue

    elif operation == 'return' and amount <= user_account_info:
        old_amount = unreturned_books[i]
        unreturned_books[i] -= amount
        print(old_amount, "=>", unreturned_books[i])
        continue
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE