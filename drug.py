import time

def line():
    print("-" * 60)

def welcome():
    line()
    print("        HOPEPATH REHABILITATION CENTER")
    line()
    print("Helping individuals recover, rebuild and restart.")
    print()
    time.sleep(1)

def show_menu():
    print("\nMAIN MENU")
    line()
    print("1. About Us")
    print("2. Programs Offered")
    print("3. Testimonials")
    print("4. Contact / Appointment")
    print("5. Exit")
    line()

def about_us():
    line()
    print("ABOUT US")
    line()
    print("HopePath Rehabilitation Center provides professional care for")
    print("individuals struggling with drug abuse. Our services include")
    print("medical detox, therapy, counselling, and long-term recovery support.")
    print()

def programs():
    line()
    print("PROGRAMS WE OFFER")
    line()
    print("1. Detoxification & Medical Support")
    print("2. Individual & Group Therapy")
    print("3. Family Counselling")
    print("4. Rehabilitation & Skill Development")
    print("5. Aftercare & Relapse Prevention")
    print()

def testimonials():
    line()
    print("TESTIMONIALS")
    line()
    print("\"HopePath changed my life. The care and support I received")
    print("helped me become myself again.\" – Former Patient")
    print()
    print("\"The counsellors were kind and patient. I felt understood")
    print("and supported throughout my recovery journey.\" – Patient's Family")
    print()

def contact():
    line()
    print("CONTACT / APPOINTMENT")
    line()
    print("Phone : +91 98765 43210")
    print("Email : support@hopepathrehab.com")
    print("Location : Pune, Maharashtra\n")
    print("Would you like to book an appointment? (yes/no)")
    
    choice = input("> ").lower()
    if choice == "yes":
        print("\nPlease enter your name:")
        name = input("> ")
        print("Please enter your phone number:")
        phone = input("> ")
        print(f"\nThank you {name}! Our team will contact you shortly at {phone}.\n")
    else:
        print("\nNo problem. You can reach out anytime.\n")

def main():
    welcome()
    while True:
        show_menu()
        choice = input("Enter your choice (1–5): ")

        if choice == "1":
            about_us()
        elif choice == "2":
            programs()
        elif choice == "3":
            testimonials()
        elif choice == "4":
            contact()
        elif choice == "5":
            print("Thank you for visiting HopePath Rehabilitation Center.")
            print("Take care and stay safe.")
            break
        else:
            print("Invalid choice. Please try again.\n")

main()