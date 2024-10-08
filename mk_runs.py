#! /usr/bin/env python3
#   script generated by source_obsnum.sh
import os
import sys

from lmtoy import runs

project="2018S1SEQUOIACommissioning"

# Dictionary of sources, each with a list of obsnum's in this project
# negative obsnums are ignored in the combinations. See also comments.txt
# for obsnum specific comments and parameters!
on = {}

# parameters for the first pass of the pipeline (restart=1 is automatically enforced here)
pars1 = {}


# parameters for the (optional) second pass of the pipeline (e.g. for bank=0)
pars2 = {}


# parameters for the (optional) third pass of the pipeline (usually for bank=1)
pars3 = {}


# Found 0 source(s) for 2018S1SEQUOIACommissioning

if __name__ == "__main__":
    runs.mk_runs(project, on, pars1, pars2, pars3, sys.argv)
