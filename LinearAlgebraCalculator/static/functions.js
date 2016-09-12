/**
  *LinearAlgebraCalculator
  * Copyright (C) 2016, Gabriel Sturtevant <Gabriel@GabrielSturtevant.com>
  *
  * This file is part of LinearAlgebraCalculator.
  *
  * LinearAlgebraCalculator is free software: you can redistribute it and/or modify
  * it under the terms of the GNU General Public License as published by
  * the Free Software Foundation, either version 3 of the License, or
  * (at your option) any later version.
  *
  * LinearAlgebraCalculator is distributed in the hope that it will be useful,
  * but WITHOUT ANY WARRANTY; without even the implied warranty of
  * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  * GNU General Public License for more details.
  *
  * You should have received a copy of the GNU General Public License
  * along with LinearAlgebraCalculator.  If not, see <http://www.gnu.org/licenses/>.
  *
  * Contributor(s):
  *
  * Gabriel Sturtevant
  *
  * Created by gabriel on 9/11/16.
  */

function set_visibility() {
			if(document.getElementById("input2").style.visibility == "visible") {
				document.getElementById("input2").style.visibility = "collapse";
				document.getElementById("row_number2").removeAttribute("required");
				document.getElementById("column_number2").removeAttribute("required");
			}
			else {
				document.getElementById("input2").style.visibility = "visible";
				document.getElementById("row_number2").setAttribute("required", "True");
				document.getElementById("column_number2").setAttribute("required", "True");
			}
		}