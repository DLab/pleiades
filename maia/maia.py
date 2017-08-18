#!/usr/bin/python3

'''
Project maia: A python3 Implementation of a Genetic Algorithm
Author: Rodrigo Santibáñez, 2017 @ Computational Biology Lab, Fundacion Ciencia y Vida (rsantibanez@dlab.cl)
An improved version from the PERL implementation of Dr Alberto Martin's Genetic Algorithm
Dr. Alberto J.M. Martin, 2016 @ Computational Biology Lab, Fundacion Ciencia y Vida (ajmm@dlab.cl)
'''

import argparse, datetime, glob, os, random, re, shlex, struct, subprocess, sys, time
import pandas

def argsparser():
	parser = argparse.ArgumentParser(description = 'Perform a parameterization employing a Genetic Algorithm.')
	parser.add_argument('--model', '-M', metavar = '\b', help = 'kappa model with tagged variables to parameterize', required = True)
	parser.add_argument('--data', '-D', metavar = '\b', help = 'tab-separated file(s) with observables to fit', required = True, nargs = '+')
	parser.add_argument('--seed', '-S', metavar = '\b', help = 'random number generator seed', type = int, required = False, default = 0)
	parser.add_argument('--binary', '-B', metavar = '\b', help = 'kappa binary prefix', required = False, default = 'model.bin')
	parser.add_argument('--output', '-O', metavar = '\b', help = 'output files prefix', required = False, default = 'outmodels')
