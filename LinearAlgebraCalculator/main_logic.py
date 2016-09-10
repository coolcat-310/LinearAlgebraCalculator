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


row_size = 0
column_size = 0


@app.route('/')
def hello_world():
	return render_template("grid.html")


@app.route('/', methods=['POST'])
def hello_world_post():
	global row_size
	global column_size
	if request.method == 'POST':
		if request.form['action'] == 'submit_dimensions':
			row_size = int(request.form['row_number'])
			column_size = int(request.form['column_number'])
			array_of_inputs = Markup("")
			for x in range(row_size):
				for y in range(column_size):
					array_of_inputs += Markup(
						"<input required=\"True\" style=\"width:40px;\" type=\"number\" name=\"input_{0}_{1}\">".format(
							x, y))
				array_of_inputs += Markup("<br>")
			return render_template("grid.html", matrix_info=array_of_inputs)
		elif request.form['action'] == 'submit_matrix':
			initial_matrix = []
			temp = []
			for x in range(row_size):
				for y in range(column_size):
					temp.append(int(request.form['input_{0}_{1}'.format(x, y)]))
				initial_matrix.append(temp)
				temp = []
			solved_matrix = (Matrix(initial_matrix).rref())[0].tolist()
			to_send = Markup("")
			for x in range(row_size):
				for y in range(column_size):
					to_send += Markup("<input required=\"True\" style=\"width:40px;\"")
					to_send += Markup(" readonly=\"True\" value=\"{2}\" name=\"input_{0}_{1}\">"
						.format(x, y, solved_matrix[x][y]))
				to_send += Markup("<br>")
			return render_template("grid.html", matrix_info=to_send)

