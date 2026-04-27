import matplotlib.pyplot as plt

def show_analytics(wards, patients):

    ward_data = {w: len(wards[w].patients) for w in wards}

    plt.bar(ward_data.keys(), ward_data.values())
    plt.title("Ward Occupancy")
    plt.xlabel("Ward")
    plt.ylabel("Patients")
    plt.show()