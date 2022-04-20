students = ['Piers Chaney', 'Riley-Jay Kidd', 'Flora Glenn', 'Amos Cooley', 'Joni Bell', 'Serenity Melia', 'Hywel Valenzuela', 'Haleemah Quintana', 'Nabeel Kendall', 'Connar Hodges', 'Belle Vaughn', 'Ryker Lowry', 'Carl Abbott', 'Sanah Hutchings', 'Kiya Bentley', 'Verity Durham', 'Aubree Luna', 'Carla Knox', 'Eduard Rosa', 'Suhail Churchill', 'Marisa Delarosa', 'Fenton Medina', 'Samad Solis', 'Anthony Wagstaff', 'Zohaib Mckeown', 'Blaine Irwin', 'Marion Donald', 'Fahima Kemp', 'Reya Naylor', 'Taran Crawford', 'Kody Welch', 'Bobby Mahoney', 'Aanya Beck', 'Natalia Pollard', 'Veronika Smith', 'Steffan Tomlinson', 'Mohammed Hansen', 'Nancie Marin', 'Arnie Leach', 'Theodor Clayton', 'Ariella Benton', 'Caitlan Conley', 'Khia Elliott', 'Dua Solomon', 'Rumaisa Petty', 'Dana Christie', 'Dhruv Alcock', 'Rodrigo Mcphee', 'Daniele Cross', 'Joseff Montoya', 'Lucinda Armstrong', 'Olive Dunlap', 'Cillian Noel', 'Latoya Villa', 'Hibba Lugo', 'Malachy Howard', 'Nathaniel Conner', 'Sharna Molloy', 'Alima Mcguire', 'Mamie Fuentes', 'Tanner Bob', 'Faraz Long', 'Nafisa Gibbs', 'Abdullahi Snider', 'Aneesha Mcculloch', 'Manraj Oliver', 'Alexis Ritter', 'Saira Escobar', 'Keir Mcleod', 'Mia-Rose Holmes', 'Rhia Roy', 'Daryl Wagner', 'Soraya Kearns', 'Kalvin Thorpe', 'Mihai Pickett', 
'Jack Bernard', 'Jacques Bains', 'Betsy Field', 'Tyler-Jay Wise', 'Arya Weiss', 'Myles Hopkins', 'Korey Frost', 'Liana Nielsen', 'Blossom Sinclair', 'Alishia Myers', 'Keiron Skinner', 'Raya Moses', 'Meera Mcfadden', 'Demi-Leigh Ochoa', 'Areeb Davis', 'Marc Webber', 'Liam Castaneda', 'Curtis Riddle', 'Carly Alston', 'Zac Preston', 'Rabia Roman', 'Iqra Whitley', 'Giorgia Piper', 'Pablo Sierra', 'Yasin Hancock']
accounts = [26.35, 7.78, 39.82, 39.79, 36.93, 27.73, 27.14, 49.14, 17.45, 44.46, 36.85, 40.35, 27.2, 13.74, 6.3, 25.21, 46.91, 15.57, 19.67, 8.78, 30.85, 37.3, 12.51, 15.64, 4.71, 30.44, 10.38, 38.73, 47.44, 30.13, 21.69, 48.15, 33.4, 6.43, 23.27, 48.95, 33.58, 35.47, 10.75, 26.76, 43.78, 12.6, 40.59, 37.25, 1.32, 3.06, 43.39, 35.51, 22.38, 47.47, 44.92, 26.25, 38.03, 49.15, 2.58, 34.84, 39.92, 32.84, 47.67, 16.21, 3.39, 4.45, 0.28, 1.54, 12.72, 5.08, 8.59, 27.8, 4.3, 24.66, 11.58, 9.83, 15.29, 20.31, 36.71, 26.17, 22.92, 33.83, 31.67, 6.9, 29.41, 
25.32, 0.38, 36.15, 23.45, 0.22, 10.81, 11.85, 40.73, 6.51, 49.93, 17.37, 15.05, 34.34, 47.79, 30.27, 5.88, 28.2, 21.96, 38.97]
# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
finished = False 
#yemekhane sim

#kahvalti = 3.5 ogle = 4 aksam = 4.5
while not finished:
    operation = input() # 'deposit' or 'reserve' or 'exit'
    while operation not in ['deposit', 'reserve', 'exit']:
        operation = input()
        
    if operation == 'exit':
        finished = True
        break
        
    user_id = input()
    while user_id not in students:
        user_id = input()
        
    if operation == 'reserve':
        meal = input()
        while meal not in ['breakfast', 'lunch', 'dinner']:
            meal = input()

    if operation == 'deposit':
        amount = int(input())
        while amount <= 0:
            amount = int(input())

    i = students.index(user_id)
    user_account_info = accounts[i]

    if operation == "deposit":
        old_amount = accounts[i]
        accounts[i] += amount
        print(old_amount, "=>", accounts[i])
        continue
        
    elif operation == "reserve":
        amount = 0
        if meal == 'breakfast':
            amount = 3.5
        elif meal == 'lunch':
            amount = 4
        elif meal == 'dinner':
            amount = 4.5
            
        if (meal == 'breakfast' and (user_account_info - 3.5) > 0) or (meal == 'lunch' and (user_account_info - 4) > 0) or (meal == 'dinner' and (user_account_info - 4.5) > 0):
            old_amount = accounts[i]
            accounts[i] -= amount
            print(old_amount, "=>", accounts[i])
            continue
        
        elif (meal == 'breakfast' and (user_account_info - 3.5) < 0) or (meal == 'lunch' and (user_account_info - 4) < 0) or (meal == 'dinner' and (user_account_info - 4.5) < 0):
            print("You don't have enough money in your card")
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE