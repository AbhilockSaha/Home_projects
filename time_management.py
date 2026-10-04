import datetime

# Function to display schedule with time slots
def display_schedule(tasks, start_time, total_hours):
    print("\n📅 Your Daily Time-Managed Schedule 📅")
    print("-" * 50)

    # Separate tasks
    immediate = [t for t in tasks if t[1] == "IMEDIATE"]
    today = [t for t in tasks if t[1] == "JUST DONE TODAY"]
    later = [t for t in tasks if t[1] == "LATER"]

    # Combine in order of importance
    ordered_tasks = immediate + today + later

    # Calculate time per task
    if len(ordered_tasks) == 0:
        print("No tasks entered. 🎉 Free day!")
        return

    time_per_task = (total_hours * 60) // len(ordered_tasks)  # in minutes
    current_time = start_time

    for i, task in enumerate(ordered_tasks, 1):
        start_str = current_time.strftime("%I:%M %p")
        current_time += datetime.timedelta(minutes=time_per_task)
        end_str = current_time.strftime("%I:%M %p")

        print(f"{i}. {task[0]}  ({task[1]})")
        print(f"   🕒 {start_str} - {end_str}\n")

    print("-" * 50)
    print("💡 Tip: Stick to the time slots to stay productive!\n")


def main():
    works = int(input("Enter how many tasks you want to do today: "))
    my_data = []

    for i in range(works):
        work = input(f"\nEnter task {i+1}: ").upper()
        importance = input("Enter priority:\n 1. Immediate\n 2. Later\n 3. Just Done Today\nChoice: ").strip()

        if importance == "1":
            importance = "IMEDIATE"
        elif importance == "2":
            importance = "LATER"
        elif importance == "3":
            importance = "JUST DONE TODAY"
        else:
            importance = "LATER"  # default

        my_data.append((work, importance))

    # Ask for available hours & start time
    total_hours = int(input("\nHow many hours do you want to work today? "))
    start_hour = int(input("Enter start hour (24-hour format, e.g., 9 for 9 AM): "))
    start_minute = int(input("Enter start minute (e.g., 0 for sharp hour): "))
    start_time = datetime.datetime.combine(datetime.date.today(), datetime.time(start_hour, start_minute))

    # Show final schedule
    display_schedule(my_data, start_time, total_hours)


if __name__ == "__main__":
    main()
