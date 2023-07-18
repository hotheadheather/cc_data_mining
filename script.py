#Run this repl_script.py to build a report of 1000 records
# It contains test data for customers and credit card data


import csv
import random
import datetime
import string


# assign names/addresses arrays with values that will be randomly paired later
def generate_data(n):

    names = ['John Smith', 'Jane Doe', 'Bob Johnson', 'Alice Brown', 'Mike Davis', 'Amy Lee', 'Tom Wilson',
             'Samantha Green', 'Mark Taylor', 'Emily Chen', 'Jackie Lee', 'David Kim', 'Sarah Lee', 'Chris Lee',
             'Peter Lee', 'Julia Chen', 'Steven Park', 'Jenny Kim', 'Patrick Wilson', 'Cindy Kim', 'Maggie Lee',
             'Erica Brown', 'Eddie Davis', 'Katie Lee', 'Daniel Lee', 'Brian Lee', 'Nancy Wilson', 'Paul Park',
             'Susan Wilson', 'Ryan Chen', 'Jasmine Kim', 'Heather Whittlesey', 'Michelle Lee', 'Lucas Kim',
             'Sophie Park', 'Max Chen', 'Sandy Kim', 'Alex Kim', 'Shirley Chen', 'Sam Lee', 'Evelyn Brown', 'Judy Lee',
             'Ethan Kim', 'Cathy Kim', 'Louis Curiel', 'Tony Chen', 'Hannah Kim', 'Matthew Lee', 'Diana Lee',
             'Holly Whittlesey', 'Lena Chen', 'Julie Park', 'Jake Kim', 'Stacy Lee', 'David Edwin', 'Lauren Kim',
             'Scott Lee', 'Grace Kim', 'Angelina Park', 'Alivia Conley', 'Tyler Chen', 'Carla Kim', 'Wendy Lee',
             'Frank Kim', 'Megan Lee', 'Andy Chen', 'Lily Kim', 'George Park', 'Ryan Conley', 'Randy Kim', 'Jill Chen',
             'Lucy Lee', 'Rachel Buse', 'Heather Kim', 'Leo Chen', 'Sodom Lee', 'Jasmine Lee', 'Nick Kim',
             'Corey Conley', 'Jerry Chen', 'Jeff Miller', 'Julian Park', 'Kathy Jeanne', 'Michael Lee', 'Jocelyn Kim',
             'Vivian Chen', 'Alexis Dwyer', 'Raymond Kim', 'Melissa Lee', 'Benjamin Park', 'Olivia Chen',
             'Bobbie Jphnsen', 'Danny Kim', 'Jenny Lee', 'Eddie David', 'Jesse Kim', 'Lindsey Hopper', 'Henry Park',
             'Annie Kim', 'Luke Chen', 'Betty Lee', 'Maxwell Kim', 'Lyndsay Nissen', 'Gregory Park', 'Kara Kim']

    addresses = [('13 Main St', 'Los Angeles', 'CA', '90001'), ('456 Elm St', 'Los Angeles', 'CA', '90210'),
                 ('7889 Oak Ave', 'Los Angeles', 'CA', '90038'), ('1011 Pine St', 'Los Angeles', 'CA', '90002'),
                 ('1213 Maple Ave', 'Newton', 'IA', '50208'), ('1415 Cedar Ln', 'Los Angeles', 'CA', '90006'),
                 ('1617 Chestnut Rd', 'Los Angeles', 'CA', '90001'), ('1819 Walnut Blvd', 'Los Angeles', 'CA', '90001'),
                 ('2020 Peachtree St', 'Atlanta', 'GA', '30303'), ('2223 Broadway', 'New York', 'NY', '10001'),
                 ('2425 Hollywood Blvd', 'Los Angeles', 'CA', '90028'), ('2627 Vine St', 'Los Angeles', 'CA', '90068'),
                 ('2859 Sunset Dr', 'Los Angeles', 'CA', '90046'), ('3031 Wilshire Blvd', 'Los Angeles', 'CA', '90010'),
                 ('3233 Rodeo Dr', 'Beverly Hills', 'CA', '90210'), ('35 Melrose Pl', 'Los Angeles', 'CA', '90029'),
                 ('3637 Robertson Blvd', 'Albuquerque', 'NM', '87194'), ('3839 Santa Monica Blvd', 'Los Angeles', 'CA', '90029'),
                 ('4041 Mulholland Dr', 'Los Angeles', 'CA', '90075'), ('42435 Benedict Canyon Dr', 'Beverly Hills', 'CA', '90210'),
                 ('4445 Laurel Canyon Blvd', 'North Hollywood', 'CA', '91607'), ('4647 Coldwater Canyon Dr', 'Waukee', 'IA', '50263'),
                 ('4849 Beverly Glen Blvd', 'Ankeny', 'IA', '50010'), ('50531 Sherman Oaks Ave', 'Sherman Oaks', 'CA', '91403'),
                 ('5455 Studio City Rd', 'Studio City', 'CA', '91604'), ('5157 North Hollywood Way', 'Burbank', 'CA', '91505'),
                 ('5859 Universal Studios Blvd', 'Universal City', 'CA', '91608'), ('6060 Hollywood Blvd', 'Los Angeles', 'CA', '90028'),
                 ('5253 Calle Cuervo Ave', 'Albuquerque', 'NM', '87194')]


# create new data array that will hold paired names/addresses as well as
    data = []
    for i in range(n):
        name = random.choice(names)
        address, city, state, zip_code = random.choice(addresses)
        credit_card = ''.join(random.choices(string.digits, k=16))
        time = datetime.datetime.now() - datetime.timedelta(days=random.randint(1, 30))
        amount = round(random.uniform(10, 50000), 2)
        id = ''.join(random.choices(string.digits, k=23))
        purchase_type = random.choice(['online', 'face-to-face'])
        signature_required = 'yes' if purchase_type == 'face-to-face' else 'no'
        data.append([name, address, city, state, zip_code, credit_card, time, amount, id, purchase_type, signature_required])
    return data


# write data to csv file
def write_csv(data, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(
            ['Name', 'Address', 'State', 'Zip', 'Credit Card', 'Time', 'Amount', 'Transaction ID', 'Purchase Type',
             'Signature Required'])
        writer.writerows(data)


# create 500000 trans
if __name__ == '__main__':
    data = generate_data(1000)
    write_csv(data, 'transactions_report.csv')
