'''
You had saved the items and their price details in a text file, which you purchased yesterday from a nearby super market.
You need to know:
1. How many items did you purchase?
2. How many items are free?
3. What is the total amount you had to pay?
4. What is the discount amount?
5. What is the final amount did you pay after the discount?
Help yourself by writing a python code to do this. Include necessary code to handle the possible exceptions.
Note:
Data is stored in a text file Purchase-1.txt.
Each line contains one item's details.
Item name and price is separated by a space.
You have to enter the file name during run time.
'''

def read_purchase_file(filename):
    try:
        with open(filename + ".txt", "r") as file:
            lines = file.readlines()

        purchased_items = 0
        free_items = 0
        amount = 0
        discount = 0
        processing = "purchase" 

        for line in lines:
            line = line.strip()
            if line == "":
                if processing == "purchase":
                    processing = "free"
                elif processing == "free":
                    processing = "discount"
                continue

            if processing == "purchase":
                try:
                    item, price = line.rsplit(" ", 1)
                    amount += float(price)
                    purchased_items += 1
                except ValueError:
                    print(f"Invalid line in purchase section: '{line}'")
            elif processing == "free":
                if "Free" in line:
                    free_items += 1
            elif processing == "discount":
                if "Discount" in line:
                    try:
                        _, dis = line.split()
                        discount = float(dis)
                    except ValueError:
                        print(f"Invalid discount format: '{line}'")

        final_amount = amount - discount

        print("Enter the file name:", filename)
        print(f"No of items purchased: {purchased_items}")
        print(f"No of free items: {free_items}")
        print(f"Amount to pay: {int(amount)}")
        print(f"Discount given: {int(discount)}")
        print(f"Final amount paid: {int(final_amount)}")

    except FileNotFoundError:
        print("Error: File not found. Please make sure the file exists.")
    except Exception as e:
        print("An unexpected error occurred:", e)

filename = input("Enter the file name: ").strip()
read_purchase_file(filename)
