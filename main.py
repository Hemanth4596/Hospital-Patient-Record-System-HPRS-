from system import HPRS

def main():
    system = HPRS()

    while True:
        print("\n1.Register")
        print("2.Admit")
        print("3.Billing")
        print("4.Search")
        print("5.Analytics")
        print("6.Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            system.add_patient()
        elif choice == '2':
            system.admit_patient()
        elif choice == '3':
            system.billing()
        elif choice == '4':
            system.search()
        elif choice == '5':
            system.analytics()
        elif choice == '6':
            break

if __name__ == "__main__":
    main()