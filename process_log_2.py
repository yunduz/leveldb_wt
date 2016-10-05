import sys, math


# class CounterExperiment(object):

#     def __init__(self):

def avg(lst):
    if(len(lst) == 0):
        return -1
    else:
        return float(sum(lst))/len(lst)

def get_mean_stddev(lst):
    if(len(lst) == 0):
        return -1, -1

    mean = avg(lst)
    deviations_sum = 0

    for item in lst:
        deviations_sum += (item - mean)**2

    variance = (1.0*deviations_sum)/len(lst)
    stddev = math.sqrt(variance)

    return mean, stddev

def process_log():
    file_in_n = sys.argv[1]
    file_out_n = sys.argv[2]


    num_threads = 0
    experiment_runs = {}
    with open(file_in_n, 'r') as f_in:
        for line in f_in:
            if not line.startswith('readseq'):
                continue
            line = line.split()
            #print line
            if line: #if line was not an empty line
                #print line
                freq = int(line[5]) # read frequency
                if freq not in experiment_runs:
                    experiment_runs[freq] = ([], [], [], [], [])
                experiment_runs[freq][0].append(float(line[1])) # micros/op
                experiment_runs[freq][1].append(float(line[2])) # MB/s
                experiment_runs[freq][2].append(float(line[3])) # elapsed time
                experiment_runs[freq][3].append(float(line[4])) # read stats?
                experiment_runs[freq][4].append(float(line[-1])) # num threads

                #print experiment_runs

    with open(file_out_n, 'w') as f_out:
        # f_out.write("num_threads,avg_elapsed_time,avg_cpu_time,"
        #             "std_dev_elapsed_time,std_dev_cpu_time\n")
        f_out.write("frequency, elapsed_time, std_dev_elapsed_time, "
                    "num_threads,avg_micros/op,std_dev_micros/op,"
                    "avg_MB/s, std_dev_MB/s\n")
        freq_nums = sorted(experiment_runs.keys())

        for freq_count in freq_nums:
            #print experiment_runs[thread_count]
            micros_op_data = get_mean_stddev(
                                    experiment_runs[freq_count][0])
            mb_s_data = get_mean_stddev(
                                    experiment_runs[freq_count][1])
            elapsed_time = get_mean_stddev(
                                    experiment_runs[freq_count][2])
            read_stats = get_mean_stddev(
                                    experiment_runs[freq_count][3])
            num_threads = get_mean_stddev(
                                    experiment_runs[freq_count][4])

            f_out.write('%d,%.6f,%.6f,%d,%.6f,%.6f,%.6f,%.6f\n' % (
                    freq_count,
                    elapsed_time[0],
                    elapsed_time[1],
                    num_threads[0], 
                    micros_op_data[0], 
                    micros_op_data[1],
                    mb_s_data[0],
                    mb_s_data[1]
                )
            )

# print get_mean_stddev([2,4,4,4,5,5,7,9])
# print get_mean_stddev([600, 470, 170, 430, 300])

process_log()