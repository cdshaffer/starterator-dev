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

    #find all available starts

    keylist = pham.stats['most_common']['annotated_starts'].keys()
    longest_genelist = keylist[0]
    sum = 0

    for start, genelist in pham.stats['most_common']['possible'].iteritems():

        if gene in genelist:
            sum += len(genelist)
            if len(genelist) > longest_genelist:
                longest_genelist = genelist


    print str(sum) + ", " + str(len(longest_genelist))

    return 8.1



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
                anomaly_score =  score_anomaly(gene, pham)
                anomalies[gene] = anomaly_score


    return anomalies

