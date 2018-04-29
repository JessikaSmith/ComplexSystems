# python 3
# simple model of SPb subway

import numpy as np
import plotly.graph_objs as go
from plotly.offline import plot
from plotly.plotly import image

station_names = {
    1: 'Devyatkino',
    2: 'Grazhdanskiy prospect',
    3: 'Akademicheskaya',
    4: 'Politekhnicheskaya',
    5: "Ploschad' Muzhestva",
    6: 'Lesnaya',
    7: 'Vyborgskaya',
    8: "Plochad' Lenina",
    9: 'Chernyshevskaya',
    10: "Ploschad' Vosstaniya/Mayakovskaya",
    11: 'Dostoevskaya/Vladimirskaya',
    12: 'Pushkinskaya/Zvenigorodskaya',
    13: 'Technologicheskiy institut 1/2',
    14: 'Baltiyskaya',
    15: 'Kirovskiy zavod',
    16: 'Avtovo',
    17: 'Leninskiy prospekt',
    18: 'Prospect veteranov',
    19: 'Parnas',
    20: 'Prospect prosvescheniya',
    21: 'Ozerki',
    22: "Udel'naya",
    23: 'Pionerskaya',
    24: 'Chornaya rechka',
    25: 'Petrogradskaya',
    26: "Gor'kovskaya",
    27: 'Nevskiy prospect/Gostiny dvor',
    28: "Spasskaya/Sadovaya/Sennaya ploshad",
    29: 'Frunzenskaya',
    30: 'Moskovskiye vorota',
    31: 'Electrosila',
    32: 'Park pobedy',
    33: 'Moskowskaya',
    34: 'Zvyozdnaya',
    35: 'Kupchino',
    36: 'Primprskaya',
    37: 'Vasileostrovskaya',
    38: "Ploshad' Aleksandra Nevskogo 1/2",
    39: 'Yelizarovskaya',
    40: 'Lomonosovskaya',
    41: 'Proletarskaya',
    42: 'Obukhovo',
    43: 'Rybatskoye',
    44: 'Ligovskiy prospekt',
    45: 'Novocherkasskaya',
    46: 'Ladozhskaya',
    47: "Prospekt bol'shevikov",
    48: 'Ulitsa dybenko',
    49: 'Komendantskiy prospekt',
    50: 'Staraya derevnya',
    51: 'Krestovskiy ostrov',
    52: 'Chkalovskaya',
    53: 'Sportivnaya',
    54: 'Admiralteyskaya',
    55: 'Obvodny kanal',
    56: 'Volkovskaya',
    57: 'Bukharestskaya',
    58: 'Mezhdunarodnaya'
}

graph = {
    1: [2],
    2: [1, 3],
    3: [2, 4],
    4: [3, 5],
    5: [4, 6],
    6: [5, 7],
    7: [6, 8],
    8: [7, 9],
    9: [8, 10],
    10: [9, 11, 27, 38],
    11: [10, 12, 28, 44],
    12: [11, 13, 28, 55],
    13: [12, 14, 28, 29],
    14: [13, 15],
    15: [14, 16],
    16: [15, 17],
    17: [16, 18],
    18: [17],
    19: [20],
    20: [19, 21],
    21: [20, 22],
    22: [21, 23],
    23: [22, 24],
    24: [23, 25],
    25: [24, 26],
    26: [25, 27],
    27: [26, 28, 37, 10],
    28: [27, 11, 12, 13, 54],
    29: [13, 30],
    30: [29, 31],
    31: [30, 32],
    32: [31, 33],
    33: [32, 34],
    34: [33, 35],
    35: [34],
    36: [37],
    37: [36, 27],
    38: [10, 39, 44, 45],
    39: [38, 40],
    40: [39, 41],
    41: [40, 42],
    42: [41, 43],
    43: [42],
    44: [11, 38],
    45: [38, 46],
    46: [45, 47],
    47: [46, 48],
    48: [47],
    49: [50],
    50: [49, 51],
    52: [51, 52],
    53: [52, 54],
    54: [53, 28],
    55: [12, 56],
    56: [55, 57],
    58: [57]
}


def get_degree_distrib():
    length_sub = [0 for i in range(6)]
    for i in graph.keys():
        print(len(graph[i]))
        length_sub[len(graph[i])] += 1
    return [i/len(graph.keys()) for i in length_sub]

def calculate_graph_metrics():
    pass

def plot_d_d(l):
    trace = go.Scatter(
        y=np.array(l[1:]),
        x=np.array([i for i in range(1, 6)]),
        mode='markers',
    )
    layout = go.Layout(
        title = 'SPb Subway degree distribution',
        xaxis=dict(
            title='k',
            type='log',
            autorange=True
        ),
        yaxis=dict(
            title='P(k)',
            type='log',
            autorange=True
        )
    )
    fig = go.Figure(data=[trace], layout=layout)
    image.save_as(fig, filename='subway_degree_distrib' + '.jpeg')


def main():
    plot_d_d(get_degree_distrib())


if __name__ == '__main__':
    main()
