# Julian A. Magrata
#Installment 5
print("========================================")
print("\t\tEXPENSIVE TRACKER")
print("\tKnow where your money goes.")
print("=" * 40)

name = input("What's your name? ")
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))

print (f"Welcome, {name}! ")

subtotal = 0
count = 0
choice = ""

while choice != "4":
    print("\nMAIN MENU")
    print("\t[1] Add an expense")
    print("\t[2] View all expenses (coming soon)")
    print("\t[3] show total spent")
    print("\t[4] Exit")

    choice = input ("Choose 1-4: ")

    if choice == "1":
     amount = float(input("Amount? "))
     subtotal += amount
     count += 1

     if amount > 200:
       print("  Huge expense - are you sure?")
     elif amount > 100:
       print("  Big expense.")
     elif amount > 50:
      print("  Moderate expense.")
     else:
      print("  Small expense.")
    
    
    elif choice == "2":
       print("Coming soon: the tracker can't remember each item yet. ")


    elif choice == "3":
        tax = subtotal * tax_percent / 100
        total = subtotal + tax
        left = budget - total

        print("\nExpenses:")
        print(f"  Count: {count}")
        print(f"  Subtotal: ${subtotal}")
        print(f"  Tax ({tax_percent}%): ${tax}")
        print(f"  Grand total: ${total}")

        if total > budget:
            print(f"Over budget by ${total - budget}!")
        elif total > budget * 0.90:
            print(f"Careful: only ${left} left.")
        else:
            print(f"Within budget. ${left} left.")

    elif choice == "4":
       print(f"Goodbye, {name}!")
       print("---------------------------------")
       print("Made by: Julian A. Magrata | Installment 5")
       print("=" * 40)
    else:
       print ("Please choose 1, 2, 3, 4.")