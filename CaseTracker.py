import json

def load_data():
    try:
        with open('case_tracker.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {'weekly_target': 9, 'daily_cases': [0] * 7, 'total_cases': 0}

def save_data(data):
    with open('case_tracker.json', 'w') as file:
        json.dump(data, file)

def show_summary(data):
    print("\n--- Weekly Case Tracker Summary ---")
    for i in range(7):
        print(f"Day {i + 1}: {data['daily_cases'][i]} cases worked.")
    print(f"\nTotal cases worked this week: {data['total_cases']}/{data['weekly_target']}")
    print(f"Remaining cases: {data['weekly_target'] - data['total_cases']}")

def add_cases(data):
    day = int(input("Enter the day number (0 for Monday, 6 for Sunday): "))
    if day < 0 or day > 6:
        print("Invalid day! Please enter a number between 0 (Monday) and 6 (Sunday).")
        return

    cases = int(input("Enter the number of cases worked: "))
    data['daily_cases'][day] += cases
    data['total_cases'] += cases
    print(f"Added {cases} cases for Day {day + 1}.")

def main():
    data = load_data()

    while True:
        print("\n--- Case Tracker ---")
        print("1. Add cases worked for a day")
        print("2. View weekly summary")
        print("3. Save progress")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_cases(data)
        elif choice == '2':
            show_summary(data)
        elif choice == '3':
            save_data(data)
            print("Progress saved!")
        elif choice == '4':
            save_data(data)
            print("Exiting the tracker...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
