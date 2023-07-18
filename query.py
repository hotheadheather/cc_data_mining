import csv
import datetime
from collections import Counter
from collections import defaultdict


# read data from csv file
def read_csv(filename):
    data = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # skip header row
        for row in reader:
            data.append(row)
    return data


# count number of unique customers
def count_unique_customers(data):
    customers = set()
    for row in data:
        name, address = row[:2]
        customer = f'{name}, {address}'
        customers.add(customer)
    return len(customers)


# count all transactions
def count_rows(data):
    return len(data)


# find max trans amount
def max_trans_amount(data):
    max_amount = 0
    for row in data:
        amount = float(row[4])
        if amount > max_amount:
            max_amount = amount
            customer_name = row[0]
    return customer_name, max_amount


# find min trans amount
def min_trans_amount(data):
    min_amount = float('inf')
    for row in data:
        amount = float(row[4])
        if amount < min_amount:
            min_amount = amount
            customer_name = row[0]
    return customer_name, min_amount


# find customers with most trans and their sum
# defaultdict provides a default value for nonexistent keys which
# is the count of customers with same name/address and sum of trans
def most_trans(data):
    count = defaultdict(int)
    total = defaultdict(float)
    for row in data:
        name = row[0]
        address = row[2]
        amount = float(row[7])
        count[(name, address)] += 1
        total[(name, address)] += amount

    sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)
    return name, address, sorted_count, total


# find date range for trans
def date_range(data):
    dates = [datetime.datetime.strptime(row[6], '%Y-%m-%d %H:%M:%S.%f') for row in data]
    start_date = min(dates)
    end_date = max(dates)
    return start_date, end_date


# find 3 most common dates for trans
def most_common_dates(data):
    dates = [datetime.datetime.strptime(row[6][:10], '%Y-%m-%d') for row in data]
    counter = Counter(dates)
    most_common = counter.most_common(3)
    common_dates = []
    for date, count in most_common:
        common_dates.append(f'{date.strftime("%Y-%m-%d")}: {count} transactions')
    return common_dates


# top five customers by transaction amount
def top_customers(data):
    customer_totals = {}
    for row in data:
        customer = row[0]
        amount = float(row[4])
        if customer in customer_totals:
            customer_totals[customer] += amount
        else:
            customer_totals[customer] = amount
    return sorted_customers[:5]


#store functions with return values in variables and print them
if __name__ == '__main__':
    data = read_csv('transactions_report_2.csv')
    num_customers = count_unique_customers(data)
    num_rows = count_rows(data)
    max_customer, max_amount = max_trans_amount(data)
    min_customer, min_amount = min_trans_amount(data)
    start_date, end_date = date_range(data)
    common_date = most_common_dates(data)
    name, address, sorted_count, total = most_trans(data)
    print(f'There are {num_customers} unique customers out of {num_rows} transactions')
    print(f'The maximum transaction amount is ${max_amount:.2f}, made by {max_customer}.')
    print(f'The minimum transaction amount is ${min_amount:.2f}, made by {min_customer}.')
    print(f'The transaction date range is from {start_date.strftime("%Y-%m-%d %H:%M:%S")} to {end_date.strftime("%Y-%m-%d %H:%M:%S")}.')
    print(f'The most common dates for transactions are {common_date}.')
    print('Top 5 customers with the most transactions:')
    for (name, address), c in sorted_count[:5]:
        print(f"{name}, {address}: {c} transactions, total amount: ${total[(name, address)]:.2f}")