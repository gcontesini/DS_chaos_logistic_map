# reset

set terminal gif animate delay 2.5
set output 'chaos_a.gif'
data_points='gnu_data_a.txt'
stats 'gnu_data_a.txt' nooutput

set xrange [0:100]
set yrange [0:1]

do for [i=1:400] {
    plot data_points index (i) w l title sprintf("%0.2f", i/100.0)
}

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# set terminal png
# set output 'chaos_c.png'

# set xrange [0:400]
# set yrange [0:1]

# data_points='gnu_data_c.txt'
# plot data_points u 1:2

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# reset

# set terminal gif animate delay 1
# set output 'chaos_b.gif'
# data_points='gnu_data_b.txt'
# stats 'gnu_data_b.txt' nooutput

# set xrange [0:0.5]
# set yrange [-10:10]

# do for [i=1:400] {
#     plot data_points index i w l
# }
