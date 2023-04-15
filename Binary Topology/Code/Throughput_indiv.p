set xrange [0:85]
set yrange [-1:8000]
set xlabel "Time"
set xzeroaxis
set ylabel "Throughput (kb/s)"
set terminal png 
set output 'final_curves/ThroughputWithoutSolution.png'
plot "curves/bb-2_Throughput_use_0_Final.txt" using 1:2 w lp title 'Throughput for router bb-2-CIFA-ATTACK',"curves/bb-3_Throughput_use_0_Final.txt" using 1:2 w lp title 'Throughput for router bb-3-CIFA-ATTACK',"curves/bb-5_Throughput_use_0_Final.txt" using 1:2 w lp title 'Throughput for router bb-5-CIFA-ATTACK',"curves/gw-3_Throughput_use_0_Final.txt" using 1:2 w lp title 'Throughput for router gw-3-CIFA-ATTACK'
set output 'final_curves/ThroughputWithSolution.png'
plot "curves/bb-2_Throughput_use_1_Final.txt" using 1:2 w lp title 'Throughput for router bb-2-MitigationSolution',"curves/bb-3_Throughput_use_1_Final.txt" using 1:2 w lp title 'Throughput for router bb-3-MitigationSolution',"curves/bb-5_Throughput_use_1_Final.txt" using 1:2 w lp title 'Throughput for router bb-5-MitigationSolution',"curves/gw-3_Throughput_use_1_Final.txt" using 1:2 w lp title 'Throughput for router gw-3-MitigationSolution'
