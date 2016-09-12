#!/usr/bin/env python
# LinearAlgebraCalculator
# Copyright (C) 2016, Gabriel Sturtevant <Gabriel@GabrielSturtevant.com>
#
# This file is part of LinearAlgebraCalculator.
#
# LinearAlgebraCalculator is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# LinearAlgebraCalculator is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with LinearAlgebraCalculator.  If not, see <http://www.gnu.org/licenses/>.
#
# Contributor(s):
#
# Gabriel Sturtevant
#
from LinearAlgebraCalculator import app
from flask import render_template, request, Markup
from sympy import Matrix


row_size1 = 0
column_size1 = 0
row_size2 = 0
column_size2 = 0
multiply = False


@app.route('/')
def hello_world():
	return render_template("grid.html", matrix_info={'is_empty': False})


@app.route('/', methods=['POST'])
def hello_world_post():
	global row_size1
	global column_size1
	global row_size2
	global column_size2
	global multiply
	if request.method == 'POST':
		if request.form['action'] == 'submit_dimensions':
			
			row_size1 = int(request.form['row_number1'])
			column_size1 = int(request.form['column_number1'])
			
			array_of_inputs1 = get_array_names(1, row_size1, column_size1)
			if request.form.getlist('Multiply'):
				multiply = True
				row_size2 = int(request.form['row_number2'])
				column_size2 = int(request.form['column_number2'])
				if column_size1 != row_size2:
					return render_template("grid.html", dimension_mismatch="Dimension mismatch", matrix_info={'is_empty': False})
				array_of_inputs2 = get_array_names(2, row_size2, column_size2)
				to_send = {'empty': array_of_inputs1, 'second_array': array_of_inputs2, 'dimension': 2, 'is_empty': True, 'is_full': False}
				return render_template("grid.html", matrix_info=to_send)
			else:
				multiply = False
				to_send = {'empty': array_of_inputs1, 'is_empty': True, 'is_full': False}
				return render_template("grid.html", matrix_info=to_send)
		
		elif request.form['action'] == 'submit_matrix':
			initial_matrix1 = []
			initial_matrix2 = []
			temp = []
			for x in range(row_size1):
				for y in range(column_size1):
					temp.append(int(request.form['input1_{0}_{1}'.format(x, y)]))
				initial_matrix1.append(temp)
				temp = []
			
			if multiply:
				for x in range(row_size2):
					for y in range(column_size2):
						temp.append(int(request.form['input2_{0}_{1}'.format(x, y)]))
					initial_matrix2.append(temp)
					temp = []
			if not multiply:
				solved_matrix = (Matrix(initial_matrix1).rref())[0].tolist()
			else:
				matrix1 = Matrix(initial_matrix1)
				matrix2 = Matrix(initial_matrix2)
				solved_matrix = (matrix1.multiply(matrix2)).tolist()
			to_send = {'solved': solved_matrix, 'is_full': True, 'is_empty': False}
			return render_template("grid.html", matrix_info=to_send)


def get_array_names(input_number, x_size, y_size):
	array_of_inputs = []
	temp_array = []
	
	for x in range(x_size):
		for y in range(y_size):
			temp_array.append("input{0}_{1}_{2}".format(input_number, x, y))
		array_of_inputs.append(temp_array)
		temp_array = []
	return array_of_inputs
