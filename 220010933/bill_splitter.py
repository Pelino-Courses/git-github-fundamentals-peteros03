Number_of_friends = int(input("Enter the number of friends joining (including you):\n"))
if Number_of_friends <= 0:
    print("No one is joining for the party")
else:
    Attendee = {}
    print("Enter the name of every friend (including you), each on a new line:")
    for names in range (Number_of_friends):
      name=input()
      Attendee[name]=0
    total_bill=float(input('Enter the total bill value:\n'))
    choices= input("Do you want to use the 'Who is lucky?'feature? Write Yes/No:\n")
    divide_bill=round(total_bill/Number_of_friends ,2)
    if choices.lower()=="yes":
        import random
        lucky=random.choice(list(Attendee.keys()))
        print(lucky, "is the lucky one!")
        Attendee[name]=0
        Friends_to_pay_bills=Number_of_friends - 1
        Second_divide_bill=round(total_bill/Friends_to_pay_bills,2)
        for d in Attendee:
            if d != lucky:
                Attendee[d]= Second_divide_bill
    else:
        print("No one lucky to day")
        for d in Attendee:
            Attendee[d]=divide_bill
    print(Attendee)
