from pyscript import display

club1 = {"Abdullah", "Escobar", "Rufo", "Choi", "Arias"}
club2 = {"Cajucom", "Enriquez", "Espin", "Arce"}

atleast_one = club1 | club2  # Students involved in at least one club
both_clubs = club1 & club2   # Students who belong to both clubs
only_in_first = club1 - club2  # Students who belong only in the first club
only_in_second = club2 - club1  # Students who belong only in the second club
exactly_one = club1 ^ club2  # Students who are in exactly one club

display(atleast_one, target="output")
display(both_clubs, target="output")
display(only_in_first, target="output")
display(only_in_second, target="output")
display(exactly_one, target="output")




