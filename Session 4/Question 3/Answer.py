citizens = [624692028, 559195285, 556197161, 918592637, 876549625, 806319354,
       582388202, 908568514, 537490623, 429223312, 815743043, 354092825,
       453976475, 909536224, 415352689, 531106990, 502586550, 769018120,
       710094895, 855926749, 747977129, 869573928, 920492135, 422251506,
       370575570, 387429979, 819467182, 778351716, 932388616, 469756066,
       345882467, 646625502, 739079546, 773639782, 370209183, 446741921,
       550934834, 470958665, 550019289, 823560332, 418928754, 624180994,
       387908792, 898059350, 833568534, 695371367, 881698853, 777985420,
       697773136, 628974760, 815109310, 393498080, 503838590, 687135510,
       485345491, 503080963, 432813601, 730513556, 713143692, 757298523,
       735034816, 567868150, 855881536, 865659418, 729558639, 467316128,
       437473752, 725793273, 446521124, 894743976, 701184482, 405074369,
       821596472, 490435448, 451024239, 666266016, 594351579, 708357204,
       742707423, 722389639, 785022802, 669639550, 839738415, 441511487,
       828993704, 433302728, 669507683, 897364360, 931945775, 860570619,
       669206487, 462641380, 577152684, 769447115, 478020794, 554312680,
       799072461, 538524688, 715301710, 376394448]
accounts = [-12.27, -33.21, -98.42, -35.82, 46.41, -16.4, 40.88, -57.53, -54.35,
            -90.57, -76.75, 4.27, 73.69, -51.18, -56.26, 2.69, 45.1, 27.07, 80.92,
            55.84, 76.76, 54.34, -48.12, 18.55, -2.2, -29.86, 48.27, -20.82,
            -48.75, -19.79, 43.39, -74.82, -98.4, -12.89, -44.74, 94.85, 24.6,
            40.4, 11.56, -26.55, 51.85, 16.13, -52.66, -91.96, -66.67, 39.33,
            10.39, -33.22, 20.94, 61.56, -68.02, 63.52, 32.47, -93.52, -2.1,
            9.01, 34.15, -53.24, -63.87, 37.84, -91.33, 47.63, -47.97, 49.29, 
            1.99, 91.55, -59.64, -92.62, -50.64, -76.16, 33.96, -21.35, 59.36, 
            11.61, -53.46, -93.09, 79.76, 51.5, 64.82, -92.46, 47.49, 65.26, -84.2,
            -55.76, -83.14, -79.27, -35.14, 52.34, -70.36, 77.97, -86.89, -95.14,
            -97.08, 31.96, 79.29, 16.4, -14.45, 15.36, 32.8, -54.34]

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE

metrobus = 7
metro=3.74
marmaray = 2.42

finished = False
maximum_amount = 100

while not finished:
    operation = input() # 'transport' or 'deposit' or 'exit'
    while operation not in ['transport', 'deposit', 'exit']:
        operation = input()
        
    if operation == 'exit':
        finished = True
        break
        
    user_id = int(input())
    while user_id not in citizens:
        user_id = int(input())
    
    if operation == "transport":
        type_of_transport = input()
        while type_of_transport not in ['metro', 'metrobus', 'marmaray']:
            type_of_transport = input()
    else:
        amount = int(input())
        while amount <= 0:
            amount = int(input())

    i = citizens.index(user_id)
    user_account_info = accounts[i]

    if operation == "transport" and user_account_info == -100: #-100e kadar avans sonra blok
        print("Your account is blocked")
        continue
    
    elif operation == "deposit" and amount > maximum_amount:
        print("You exceeded the maximum allowed deposit amount")
        continue
    
    elif operation == "deposit":
        old_amount = accounts[i]
        accounts[i] += amount
        print(old_amount, "=>", accounts[i])
    
    elif (user_account_info >= metro or metrobus or marmaray) and operation == "transport":
        if (type_of_transport == 'metro' and (user_account_info - metro) < -100) or (type_of_transport == 'metrobus' and (user_account_info - metrobus < -100)) or (type_of_transport == 'marmaray' and (user_account_info - marmaray < -100)):
            print("Inadequate balance")
            
        else:
            money = 0
            if type_of_transport == 'metro':
                money = metro
            elif type_of_transport == 'metrobus':
                money = metrobus
            elif type_of_transport == 'marmaray':
                money = marmaray
            old_amount = accounts[i]
            accounts[i] -= money
            print(old_amount, "=>", accounts[i])
        

        
# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE