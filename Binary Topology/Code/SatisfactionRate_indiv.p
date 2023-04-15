set xrange [0:85]
set yrange [-1:120]
set xlabel "Time"
set xzeroaxis
set ylabel "Satisfaction Rate(%)"
set terminal png 
set output 'final_curves/SatisfactionRateWithoutSolution.png'
plot "curves/good-leaf-10_SatisfactionRate_use_0_Final.txt" using 1:2 w lp title 'Satisfaction Rate for good-leaf-10-CIFA-ATTACK'
set output 'final_curves/SatisfactionRateWithSolution.png'
plot "curves/good-leaf-10_SatisfactionRate_use_1_Final.txt" using 1:2 w lp title 'Satisfaction Rate for good-leaf-10-MitigationSolution'
