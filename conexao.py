# coding=utf-8

class Conexao:
	peso = 0.0

	def __init__(self, peso=0.0):
		self.peso = peso

	def __str__(self):
		return "{}".format(self.peso)

	def set_peso(self, peso):
		self.peso = peso
