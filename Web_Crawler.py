import csv
import random
import names

computer_science_universities = [
    "MIT",
    "Stanford University",
    "Carnegie Mellon University",
    "UC Berkeley",
    "Princeton University",
    "Harvard University",
    "Caltech",
    "Cornell University",
    "University of Chicago",
    "Columbia University",
    "New York University",
    "Rice University",
    "University of Texas - Austin",
    "University of Illinois - Urbana-Champaign",
    "University of Maryland - College Park",
    "University of Pennsylvania",
    "Yale University",
    "Cambridge",
    "Berkley",
    "Oxford University",
    "Johns Hopkins University",
    "University of College London",
    "Tsinghua University",
    "Ohio State University",
    "University of Tokyo",
    "National University of Singapore",
    "University of Pittsburgh",
    "McGill University",
    "Nanyang Technological University",
    "University of Melbourne",
    "Catholic University of Leuven",
    "University of Sydney",
    "Shanghai Jiao Tong University"
    "University of California--Irvine"
    "CEID University of Patras"
]


class Scientist(object):
    def __init__(self, s, a, d, e):
        self.surname = s
        self.awards = a
        self.description = d
        self.education = e


def generate_data(length):
    # Define the filename of the CSV file
    filename = "WikiScientists_short.csv"

    # Open the CSV file in UTF-8 encoding
    with open(filename, encoding="UTF-8") as file:
        # Convert all capital letters to small letters
        data = file.read().lower()

        # Create a CSV reader object
        reader = csv.reader(data.splitlines())

        # Extract the data from the CSV file
        scientists = []
        row_count = 0  # Initialize the counter
        for row in reader:
            try:
                name, description = row[0].split(" - ")
            except ValueError:
                continue
            surname = name.split()[-1]
            awards = random.randint(0, 30)
            education = random.sample(computer_science_universities, 5)
            # Create a new Scientist object and append it to the list
            scientists.append(Scientist(surname, awards, description, education))
            row_count += 1  # Increment the counter

        # Print the extracted data
        for scientist in scientists:
            print(
                f"Surname: {scientist.surname} (CSV scientist),\t Awards: {scientist.awards},\t Education: {scientist.education},\t Description: {scientist.description}")

        # Add randomly generated scientists if necessary
        if length > row_count:
            # Create a list of existing surnames
            used_surnames = [scientist.surname for scientist in scientists]
            for i in range(length - row_count):
                surname = names.get_last_name().lower()
                while surname in used_surnames:
                    surname = names.get_last_name().lower()
                used_surnames.append(surname)
                awards = random.randint(0, 30)
                education = random.sample(computer_science_universities, 5)
                # Set the description to an empty string
                scientist = Scientist(surname, awards, "", education)
                scientists.append(scientist)
                # Print the scientist object
                print(
                    f"Surname: {scientist.surname},\t Awards: {scientist.awards},\t Education: {scientist.education},\t Description: {scientist.description}")

        # Print the number of rows
        print(f"Number of rows: {len(scientists)}")
        data = scientists
        return data
