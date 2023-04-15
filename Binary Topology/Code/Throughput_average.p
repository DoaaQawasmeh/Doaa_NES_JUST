set xrange [0:85]
set yrange [-1:8000]
set xlabel "Time"
set xzeroaxis
set ylabel "Throughput (kb/s)"
set terminal png 
set output 'final_curves/AverageThroughputWithoutSolution.png'
plot "curves/average/AverageThroughput_use_0_Final.txt" using 1:2 w lp title 'Throughput for good-consumers-CIFA-ATTACK'
set output 'final_curves/AverageThroughputWithSolution.png'
plot "curves/average/AverageThroughput_use_1_Final.txt" using 1:2 w lp title 'Throughput for good-consumers-MitigationSolution'
