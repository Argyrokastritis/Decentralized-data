from Web_Crawler import generate_data
from pastry import PastryNode
from chord import ChordNode
from chord import ChordNetwork

if __name__ == '__main__':
    length = input("""How many rows of data do you want to generate? (~200 recommended) """)
    scientists_data = generate_data(int(length))
    mode = input("""Choose operation mode:\n\t0: CHORD\n\t1: PASTRY\n\t""")
    mode = int(mode)

    min_sur = input("""Minimum surname for range query: """)
    max_sur = input("""Maximum surname for range query: """)
    min_aw = input("""Minimum awards for range query: """)
    max_aw = input("""Maximum awards for range query: """)
    min_aw = int(min_aw)
    max_aw = int(max_aw)
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

# Ask user if they want to exit
ans = input("""\n\n\nDo you want to exit the decentralized algorithms project?""")
if ans == 'y':
    exit()
