import os
import sys
import subprocess
import re

#Recebe um vetor com os valores das variaveis a serem testadas
#retorna o percentual do cdg que foi coberto

def test_arq(values, html= False):
    name_file = 'test_file.py'
    cmd = "coverage run --omit "+name_file+" "+name_file

    for v in values:
        cmd = cmd + " "+str(v)

    os.system(cmd)
    os.system("coverage report")

    var = subprocess.check_output(
        ["coverage", "report"],
        stderr=subprocess.STDOUT,
        shell=True).decode('utf-8')

    if html:
        os.system("coverage html")

    test = var.split('\n')

    line = test[2]
    value = re.findall(r"[\w']+", line)[-1]

    #print(value)
    return value
