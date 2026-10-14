import datetime 


def run_data_collector():
    # ----------------------------------------------------
    # 1. WELCOME MESSAGE & APPLICATION OVERVIEW
    # ----------------------------------------------------
    print("=" * 60)
    print("      WELCOME TO THE PERSONAL DATA COLLECTOR APP      ")
    print("=" * 60)
    print("About this Application:")
    print("• Captures personal details through interactive prompts.")
    print("• Processes and calculates your age based on your birth year.")
    print("• Inspects internal memory locations using id().")
    print("• Analyzes variable data types using type().")
    print("-" * 60)

    # ----------------------------------------------------
    # 2. DATA COLLECTION (INPUTS)
    # ----------------------------------------------------
    print("\n--- STEP 1: Enter Your Information ---")

    name = input("Enter your full name: ")

    birth_year_str = input("Enter your birth year : ")
    birth_year = int(birth_year_str)

    height_str = input("Enter your height in meters : ")
    height = float(height_str)

    fav_num_str = input("Enter your favorite number: ")
    fav_num = int(fav_num_str)

    # ----------------------------------------------------
    # 3. DATA PROCESSING
    # ----------------------------------------------------
    # Get current year dynamically
    current_year = datetime.datetime.now().year
    calculated_age = current_year - birth_year

    # ----------------------------------------------------
    # 4. DISPLAY SUMMARY & TECHNICAL INSPECTION
    # ----------------------------------------------------
    print("\n" + "=" * 60)
    print("               PERSONAL DATA SUMMARY                  ")
    print("=" * 60)

    print(f"Name:             {name}")
    print(f"Birth Year:       {birth_year}")
    print(f"Calculated Age:   {calculated_age} years old (in {current_year})")
    print(f"Height:           {height} m")
    print(f"Favorite Number:  {fav_num}")

    print("\n" + "-" * 60)
    print("         TECHNICAL INSPECTION (Data Types & Memory)   ")
    print("-" * 60)

    print(
        f"Variable 'name':\n  Value: {name}\n  Type: {type(name)}\n  Memory ID: {id(name)}\n"
    )

    print(
        f"Variable 'birth_year':\n  Value: {birth_year}\n  Type: {type(birth_year)}\n  Memory ID: {id(birth_year)}\n"
    )

    print(
        f"Variable 'calculated_age':\n  Value: {calculated_age}\n  Type: {type(calculated_age)}\n  Memory ID: {id(calculated_age)}\n"
    )

    print(
        f"Variable 'height':\n  Value: {height}\n  Type: {type(height)}\n  Memory ID: {id(height)}\n"
    )

    print(
        f"Variable 'fav_num':\n  Value: {fav_num}\n  Type: {type(fav_num)}\n  Memory ID: {id(fav_num)}\n"
    )

    # ----------------------------------------------------
    # 5. CLOSING / THANK YOU MESSAGE
    # ----------------------------------------------------
    print("=" * 60)
    print(" Thank you for using the Personal Data Collector App! ")
    print("           Have a fantastic day ahead!                ")
    print("=" * 60)


# Run the application
if __name__ == "__main__":
    run_data_collector()
