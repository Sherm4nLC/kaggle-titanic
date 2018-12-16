# -*- coding: utf-8 -*-

import pandas as pd
import tensorflow as tf
from datetime import datetime as dt

'''
The intention is to create the submission files
starting from the provided dataset
'''

class ProcessTitanic(object):
	def __init__(self):
		self.init_time = dt.now()
		self.data = None
		pass

	def load_data(self):
		self.data = 1

if __name__=="__main__":
	pt = ProcessTitanic()
	print(pt.init_time)
	pt.load_data()
	print(pt.data)
