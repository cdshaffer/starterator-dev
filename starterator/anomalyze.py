#!/usr/bin/env python
# Copyright (c) 2016 All Right Reserved
#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY
# KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A
# PARTICULAR PURPOSE.  USE AT YOUR OWN RISK.
#
# Chris Shaffer
# July 10, 2016
# Anomalyzer function


def score_anomaly(gene, pham):
    print "scoring level of anomaly for gene " + gene

    #find most annotated start of the available starts in the gene

    available_alignment_starts = pham.genes[gene].alignment_candidate_starts
    available_starts = [ pham.total_possible_starts.index(aas)+1 for aas in available_alignment_starts]

    #find the most numberous of the annotated starts out of the list of available
    max_count = 0
    for start_index in available_starts:
        if start_index in pham.stats['most_common']['annotated_starts'].keys():
            if pham.stats['most_common']['annotated_counts'][start_index] > max_count:
                max_count = pham.stats['most_common']['annotated_counts'][start_index]
                max_index = start_index

    # max_count has the number of genes with the maximum number of annotations of all starts in gene
    # max_index in the index of that start with max



    max_power =  pham.stats['most_common']['annotated_power'][max_index]

    return max_power, max_index



def anomalyzer(pham, level=1):
    print "Start anomalization on pham: " + pham.pham_no
    start_counts = pham.stats['most_common']['annotated_counts']
    starts = pham.stats['most_common']['annotated_starts']
    #check if any annotated starts agree with level or fewer genes (i.e. level 1 = unique call, level 2 has one other match

    if min(start_counts.values()) > level:
        return None

    anomalies = {}
    for key, value in starts.iteritems():
        if len(starts[key]) <= level:
            for gene in value:
                best_candidate_power, best_candidate_index =  score_anomaly(gene, pham)
                anomalies[gene] = {best_candidate_index:best_candidate_power}


    return anomalies

