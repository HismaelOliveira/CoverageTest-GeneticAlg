import GeneticAlg as ga
import pandas as pd
from random import *

def get_genes_from(fn):
    df = pd.read_csv(fn)
    print(df)
    genes = []

    genes = [ga.Gene(row['variavel'], int(randrange(float(row['minValue']), float(row['maxValue'])))) for _, row in df.iterrows()]

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
