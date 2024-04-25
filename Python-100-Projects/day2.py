if __name__ == "__main__":
    print("Welcome to the Tip Calculator!")

    bill = float(input("What was the total bill? "))
    tip_pct = input("How much tip would you like to give? 10, 12 or 15? ")
    tip_multiplier = float(f"1.{tip_pct}")
    people_ct = int(input("How many people to split the bill? "))

    total_cost = bill * tip_multiplier
    per_person_cost = total_cost / people_ct
    print(f"Each person should pay {round(per_person_cost, 2)}")