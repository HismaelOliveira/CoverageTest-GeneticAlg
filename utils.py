import GeneticAlg as ga
import pandas as pd
from random import random

def get_genes_from(fn, dt):
    df = pd.read_csv(fn)

    genes = [ga.Gene(row['variavel'], row['tipo'](random(row['minValue'], row['maxValue'])))
             for _, row in df.iterrows()]

    return genes

def plot(individual):
    print()
    print('-- Security-GA -- Caso de Teste ')


    for p in individual.genes:
        print(p.name+"  ")
    print()
    print('------------------------')
    print('Fitness: ', individual.__fitness)
    print('------------------------')
