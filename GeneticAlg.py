from sys import maxsize
from time import time
from math import ceil
from random import random, randint, sample
import utils
import TestCoverage

class Gene:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Individual:
    def __init__(self, genes):
        assert(len(genes)>3)
        self.genes = genes
        self.__reset_params()

    def __reset_params(self):
        self.__fitness = 0.0

    def swap(self, gene1, gene2):
        self.genes[0]
        a, b, = self.genes.index(gene1), self.genes.index(gene2)
        self.genes[b], self.genes[a] = self.genes[a], self.genes[b]
        self.__reset_params()

    def add(self, gene):
        self.genes.append(gene)
        self.__reset_params()

    @property
    def fitness(self):
        if self.__fitness == 0.0:
            x = [a.value for a in self.genes]
            print(x)
            self.__fitness = TestCoverage.test_arq(x)
        return self.__fitness

class Population:
    def __init__(self, individuals):
        self.individuals = individuals

    @staticmethod
    def gen_individuals(sz, genes):
        individuals = []
        for _ in range(sz):
            individuals.append(Individual(sample(genes, len(genes))))
        return Population(individuals)

    def add(self, entries):
        self.individuals.append(entries)

    def rmv(self, entries):
        self.individuals.remove(entries)

    #Retornar a melhor individuo a população
    def get_fittest(self):
        fittest = self.individuals[0]
        for entrie in self.individuals:
            if entrie.fitness < fittest.fitness:
                fittest = entrie
        return fittest

#METODOS DO ALGORITMO GENÉTICO

def evolve(pop, tourn_size, mut_rate):
    new_generation = Population([])
    pop_size = len(pop.individuals)
    elitism_num = pop_size//2

    for _ in range(elitism_num):
        fittest = pop.get_fittest()
        new_generation.add(fittest)
        pop.rmv(fittest)

    for _ in range(elitism_num, pop_size):
        parent1 = selection(new_generation, tourn_size)
        parent2 = selection(new_generation, tourn_size)
        child = crossover(parent1, parent2)
        new_generation.add(child)

    for i in range(elitism_num, pop_size):
        mutate(new_generation.individuals[i], mut_rate)

    return new_generation

def crossover(parent1, parent2):
    def fill_with_parent1_genes(child, parent, genes_n):
        start_at = randint(0, len(parent.genes)-genes_n-1)
        finish_at = start_at + genes_n
        for i in range(start_at, finish_at):
            child.genes[i] = parent1.genes[i]

    def fill_with_parent2_genes(child, parent):
        j = 0
        for i in range(0, len(parent.genes)):
            if child.genes[i] == None:
                while parent.genes[j] in child.genes:
                    j += 1
                child.genes[i] = parent.genes[j]
                j += 1

    genes_n = len(parent1.genes)
    child = Individual([None for _ in range(genes_n)])
    fill_with_parent1_genes(child, parent1, genes_n // 2)
    fill_with_parent2_genes(child, parent2)

    return child

def mutate(individual, rate):
    for _ in range(len(individual.genes)):
        if random() < rate:
            sel_genes = sample(individual.genes, 1)
            pos = int(random())
            sel_genes[pos] = int(random())

def selection(population, competitors_n):
    return Population(sample(population.individuals, competitors_n)).get_fittest()

def run_ga(genes, pop_size, n_gen, tourn_size, mut_rate):
    population = Population.gen_individuals(pop_size, genes)
    history = {'cost': [population.get_fittest().__fitness]}
    counter, generations, min_cost = 0, 0, maxsize

    print("-- Security-GA -- Inicializando Evolução...")
    start_time = time()
    while generations < n_gen:
        population = evolve(population, tourn_size, mut_rate)
        cost = population.get_fittest().__fitness

        if cost < min_cost:
            counter, min_cost = 0, cost
        else:
            counter += 1

        generations += 1
        history['cost'].append(cost)

    total_time = round(time() - start_time, 6)
    print("-- Security-GA -- Evolução finalizada após {} gerações em {} s".format(generations, total_time))
    #print("-- Security-GA -- Custo Mínimo {} ".format(min_cost))

    history['generations'] = generations
    history['total_time'] = total_time
    history['testCase'] = population.get_fittest()

    return history
