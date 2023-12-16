from Web_Crawler import generate_data
from pastry import PastryNode
from chord import ChordNode
from chord import ChordNetwork
import time
from statistics import mean

if __name__ == '__main__':
    # Get number of rows to generate
    while True:
        length = input("""How many rows of data do you want to generate? (~200 recommended) """)
        if length.isdigit():
            length = int(length)
            break
        else:
            print("Please enter a valid integer for length.")

    scientists_data = generate_data(length)

    # Get operation mode
    while True:
        mode = input("""Choose operation mode:\n\t0: CHORD\n\t1: PASTRY\n\t""")
        if mode.isdigit() and int(mode) in [0, 1]:
            mode = int(mode)
            break
        else:
            print("Please enter a valid integer (0 or 1) for mode.")

    # Get range query parameters
    while True:
        min_sur = input("""Minimum surname for range query: """)
        max_sur = input("""Maximum surname for range query: """)
        if min_sur.isalpha() and max_sur.isalpha() and min_sur <= max_sur:
            break
        else:
            print("Please enter valid surnames for range query.")

    while True:
        min_aw = input("""Minimum awards for range query: """)
        max_aw = input("""Maximum awards for range query: """)
        if min_aw.isdigit() and max_aw.isdigit() and int(min_aw) <= int(max_aw):
            min_aw = int(min_aw)
            max_aw = int(max_aw)
            break
        else:
            print("Please enter valid integers for awards range query.")

    education = input("""College to search for: """)


    if mode == 0:
        education_data = []
        for scientist in scientists_data:
            education_data.append(scientist.education)
        # print(education_data)

        # Create a new ChordNode object
        node = ChordNode(0, {}, None, scientists_data)

        # Create a new ChordNetwork object
        network = ChordNetwork()

        # Add the node to the network
        # network.add_node(node)
        node.join(network)

        # Perform a lookup operation with the given parameters
        lookup_results = network.chord_lookup(education_data, education, min_aw, max_aw, min_sur, max_sur)

        # extract the objects of scientists whose surnames match the list `lookup_results`
        lookup_results = [scientist for scientist in scientists_data if scientist.surname in lookup_results]

        # print(lookup_results)
        if lookup_results is []:
            print("Unfortunately NO matches found please try with different inputs this time")
        # Print the results
        print(f'Found {len(lookup_results)} matches:')
        for res in lookup_results:
            print(f"""\tSurname: {res.surname}\n\tAwards: {res.awards}\n\tEducation: {res.education}\n\t------""")

    if mode == 1:
        # Create a new PastryNode object
        node = PastryNode(0, scientists_data)
        # Perform a lookup operation with min_aw as threshold
        results = node.lookup(education, min_aw, max_aw, min_sur, max_sur)

        # Print the results
        print(f'Found {len(results)} matches:')
        for res in results:
            print(f"""\tSurname: {res.surname}\n\tAwards: {res.awards}\n\tEducation: {res.education}\n\t------""")


def column(matrix, i):
    return [row[i] for row in matrix]


def experiments():
    scale = 200
    query_times = []
    print('\nNow it is going to run the iterations wait a minute or less for the procedure to be completed\n')
    for i in range(100):
        print(f'Iteration {i + 1}/100 running...')
        new_query_row = []
        exp_scientists_data = generate_data(100)
        min_sur = 'b'
        max_sur = 'h'
        min_aw = 5
        max_aw = 15
        education = 'MIT'

        start = time.time()
        exp_education_data = []
        for scientist in exp_scientists_data:
            education_data.append(scientist.education)
        # print(education_data)

        # Create a new ChordNode object
        node = ChordNode(0, {}, None, scientists_data)

        # Create a new ChordNetwork object
        exp_network = ChordNetwork()

        # Add the node to the network
        # network.add_node(node)
        node.join(network)

        # Perform a lookup operation with the given parameters
        exp_lookup_results = network.chord_lookup(education_data, education, min_aw, max_aw, min_sur, max_sur)

        # extract the objects of scientists whose surnames match the list `lookup_results`
        exp_lookup_results = [scientist for scientist in scientists_data if scientist.surname in exp_lookup_results]
        end = time.time()
        new_query_row.append(end - start)

        start = time.time()
        # Create a new PastryNode object
        exp_node = PastryNode(0, scientists_data)
        # Perform a lookup operation with min_aw as threshold in Pastry lookup
        exp_results = exp_node.lookup(education, min_aw, max_aw, min_sur, max_sur)
        end = time.time()
        new_query_row.append(end - start)

        query_times.append(new_query_row)

    print('\n\nExperiment results:')
    print(f'Chord average query time miliseconds: {1000 * mean(column(query_times, 0)) / scale}')
    print(f'Pastry average query time miliseconds: {1000 * mean(column(query_times, 1)) / scale}')


exper_answer = input("""\n\nWould you like to run the experiments? Please answer with y for yes and n for no  """)
# print(exper_answer)
if exper_answer.lower() == 'y':
    experiments()

elif exper_answer.lower() == 'n':
    print('Next time please consider running them to see the efficiency of each algorithm in time')

# Ask user if they want to exit
ans = input("""\n\n\nDo you want to exit the decentralized algorithms project?  """)
if ans == 'y' or ans == 'Y':
    exit()

elif ans == 'N' or ans == 'n':
    print("\n\nThe procedure has finished if you'd like to restart the procedure re-run the program")
    time.sleep(5)
    exit()
