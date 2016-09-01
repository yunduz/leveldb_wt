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
                num_threads = int(line[-1])
                if num_threads not in experiment_runs:
                    experiment_runs[num_threads] = ([], [])
                experiment_runs[num_threads][0].append(float(line[1]))
                experiment_runs[num_threads][1].append(float(line[2]))

                #print experiment_runs

    with open(file_out_n, 'w') as f_out:
        # f_out.write("num_threads,avg_elapsed_time,avg_cpu_time,"
        #             "std_dev_elapsed_time,std_dev_cpu_time\n")
        f_out.write("num_threads,avg_micros/op,std_dev_micros/op,"
                    "avg_MB/s, std_dev_MB/s\n")
        thread_nums = sorted(experiment_runs.keys())

        for thread_count in thread_nums:
            #print experiment_runs[thread_count]
            micros_op_data = get_mean_stddev(
                                    experiment_runs[thread_count][0])
            mb_s_data = get_mean_stddev(
                                    experiment_runs[thread_count][1])

            f_out.write('%d,%.6f,%.6f,%.6f,%.6f\n' % (thread_count, 
                                                  micros_op_data[0], 
                                                  micros_op_data[1],
                                                  mb_s_data[0],
                                                  mb_s_data[1]))

# print get_mean_stddev([2,4,4,4,5,5,7,9])
# print get_mean_stddev([600, 470, 170, 430, 300])

process_log()