reset


# pause -1

set terminal png
set output "feigenbaum_diagram_exp.png"

set xrange[1:4]

set xlabel "r"
set ylabel "Orbit"

plot "feigenbaum_diagram.txt" u 1:2 ps 0.1 lc black notitle

reset