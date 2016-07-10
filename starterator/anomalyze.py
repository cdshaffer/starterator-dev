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


def anomalyze(pham, level=1):
    print "Start anomalization on pham: " + pham.pham_no

    #check if any annotated starts agree with level or fewer genes (i.e. level 1 = unique call, level 2 has one other match

    if min(pham.stats['most_common']['annotated_counts']) <= level:    #pham has at least one that needs reporting
