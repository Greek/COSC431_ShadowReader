from datetime import datetime, timedelta

def main():
    SHADOW_PATH = "./shadow.txt"
    shadow_entries = []

    with open(SHADOW_PATH) as file:
        for entry in file:
            curr_entry = entry.split(":")
            shadow_entries.append(curr_entry)

    for entry in shadow_entries:
        last_change_date = datetime(1970, 1, 1) + timedelta(days=int(entry[2]))
        formatted_date = last_change_date.strftime('%Y-%m-%d')

        print(f"User {entry[0]}'s password was last changed on {formatted_date}.")

if __name__ == "__main__":
    main()
