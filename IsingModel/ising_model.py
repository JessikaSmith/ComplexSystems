# python 3

import random
from numpy import *

import plotly.graph_objs as go
from plotly.offline import plot
from plotly.plotly import image


class real_node:

    def __init__(self, name):
        self.name = name
        self.spin = 0
        self.neigh = []
        self.neigh_temp = []
        self.neigh_temp_w = []
        self.degree = 0

    def AddNeigh(self, new):
        self.neigh.append(new)

    def setDegree(self):
        self.degree = len(self.neigh)

    def UpdateSpin(self, spin):
        self.spin = spin


def weighted_choice(weights):
    totals = []
    running_total = 0

    for w in weights:
        running_total += w
        totals.append(running_total)

    rnd = random.random() * running_total
    for i, total in enumerate(totals):
        if rnd < total:
            return i


def compute_magnetization(agents):
    mag = 0.0
    for i in agents:
        mag += i.spin
    return mag / len(agents)


def compute_energy(random_agent, current_spin, neigh_list, agents):
    energy = 0.0
    for w in neigh_list:
        energy = energy + current_spin * agents[w].spin
    energy = energy * (-1)
    return energy


def run_ising(agents, Temperature, time_step):
    for k in range(time_step):
        random_agent = random.randint(0, len(agents) - 1)
        its_spin = agents[random_agent].spin
        neigh_list = agents[random_agent].neigh
        initial_energy = compute_energy(random_agent, its_spin, neigh_list, agents)
        inverse_spin = its_spin * (-1)
        second_energy = compute_energy(random_agent, inverse_spin, neigh_list, agents)
        delta_energy = second_energy - initial_energy

        if delta_energy <= 0:
            agents[random_agent].UpdateSpin(inverse_spin)
        else:
            probability_change = exp(-delta_energy / Temperature)
            prob_list = [probability_change, 1.0 - probability_change]
            result = weighted_choice(prob_list)
            if result == 0:
                agents[random_agent].UpdateSpin(inverse_spin)
    mag = compute_magnetization(agents)
    return mag


def generate_lattice_2d(nr_agent):
    lista_starting = []
    x = 0
    w = 0
    while (x < nr_agent):
        y = x
        w = 0
        while (w < (sqrt(nr_agent) - 1)):
            lista_starting.append((y, y + 1))
            lista_starting.append((y + 1, y))
            y += 1
            w += 1
        x += int(sqrt(nr_agent))
    x = 0
    w = 0
    while (x < sqrt(nr_agent)):
        y = x
        w = 0
        while (w < (nr_agent - sqrt(nr_agent))):
            lista_starting.append((int(y + sqrt(nr_agent)), y))
            lista_starting.append((y, (int(y + sqrt(nr_agent)))))
            y += int(sqrt(nr_agent))
            w += sqrt(nr_agent)
        x += 1
    x = 0
    y = 0
    while (x < sqrt(nr_agent)):
        y = x + (sqrt(nr_agent) - 1) * sqrt(nr_agent)
        lista_starting.append((x, int(y)))
        lista_starting.append((int(y), x))
        x += 1
    x = 0
    y = 0
    while (x < nr_agent):
        y = x + sqrt(nr_agent) - 1
        lista_starting.append((x, int(y)))
        lista_starting.append((int(y), x))
        x += int(sqrt(nr_agent))
    return lista_starting


def get_neighs(my_lattice, k):
    my_list = []
    for w in my_lattice:
        if w[0] == k:
            my_list.append(w[1])
    return my_list


def initiate_spin(agents, random_spin, k):
    if random_spin == 0:
        my_spin = 1
    elif random_spin == 1:
        my_spin = -1
    else:
        print("Error spin")
    agents[k].UpdateSpin(my_spin)


def init_conf(n_agents, my_lattice):
    agents = []
    for k in range(n_agents):
        agents.append(real_node(k))
        random_spin = random.randint(0, 1)
        initiate_spin(agents, random_spin, k)
        agents[k].neigh = get_neighs(my_lattice, k)
    return agents


def plot_res(temp, magnetization):
    trace = go.Scatter(
        x=temp,
        y=[abs(mag) for mag in magnetization],
        mode='lines+markers'
    )
    layout = dict(title='Magnetization dynamics',
                  xaxis=dict(title='T'),
                  yaxis=dict(title='M'),
                  )
    data = [trace]
    fig = go.Figure(data=data, layout=layout)
    plot(fig, image_filename="test.png")
    # image.save_as(fig, filename='temp_magnetization' + '.jpeg')


def experiment():
    n_agent = 100
    time_step = 10000
    n_simulations = 30
    avg_magnetization = []
    temp = []
    for t in range(10, 81, 1):
        mag_list = []
        for w in range(n_simulations):
            my_lattice = generate_lattice_2d(n_agent)
            agents = init_conf(n_agent, my_lattice)
            magnetization = run_ising(agents, t / 10, time_step)
            mag_list += [magnetization]
        avg_magnetization += [sum(mag_list) / len(mag_list)]
        temp += [t / 10]
    plot_res(temp, avg_magnetization)


def main():
    experiment()


if __name__ == '__main__':
    main()
