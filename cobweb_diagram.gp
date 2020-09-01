reset

# set terminal epslatex standalone color 12

set terminal gif animate delay 0.5

set xrange[0:1]
set yrange[0:1]

set xlabel "x"
set ylabel "r*x*(1-x)"

set output "cobweb_diagram_r_.gif"
cobweb_data = "cobweb_diagram.txt"

do for [i_int=1:400-1] {

  plot (i_int/100.0)*x*(1-x) notitle
  replot x notitle
  replot cobweb_data index i_int u 1:2 with lp lc rgb "black" title  sprintf("Value of r :%.4f",i_int/100.0)

}

# cobweb_data = "cobweb_2.5.txt"
# plot 2.5*x*(1-x) notitle
# replot x notitle
# replot cobweb_data u 1:2 with lp lc rgb "black" notitle  
# set output "cobweb_diagram_r_2.5.png"
# replot

# cobweb_data = "cobweb_3.2.txt"
# plot 3.2*x*(1-x) notitle
# replot x notitle
# replot cobweb_data u 1:2 with lp lc rgb "black" notitle  
# set output "cobweb_diagram_r_3.2.png"
# replot

# cobweb_data = "cobweb_3.6.txt"
# plot 3.6*x*(1-x) notitle
# replot x notitle
# replot cobweb_data u 1:2 with lp lc rgb "black" notitle  
# set output "cobweb_diagram_r_3.6.png"
# replot

reset