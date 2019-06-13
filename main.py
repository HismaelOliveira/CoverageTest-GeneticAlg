import utils
import random
import argparse
import GeneticAlg as ga
from datetime import datetime

variaveis = 'variaveis.csv'
pop_size = 20
n_gen = 10
tourn_size = 5
mut_rate = 0.05

genes = utils.get_genes_from(variaveis)
history = ga.run_ga(genes, pop_size, n_gen, tourn_size, mut_rate)

utils.plot(history['testCase'])
