import subprocess
import fileinput

output = subprocess.check_output(['./phrases_counter',
                                  'origin_of_species.txt'])

lines = output.split("\n")

assert "320 - " in lines[0]
assert "33 - " in lines[99]
print "Tests pass"
