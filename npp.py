# Copyright 2020 D-Wave Systems Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

## ------- import packages -------
from dwave.system import DWaveSampler, EmbeddingComposite

# TODO:  Add code here to define your QUBO dictionary
def define_QUBO(S):

    Q = {}

    # Add QUBO construction here
    
    return Q

# TODO:  Choose QPU parameters in the following function
def run_on_QPU(Q, sampler):

    chainstrength = 1 # update
    numruns = 1 # update

    sample_set = sampler.sample_qubo(Q, chain_strength=chainstrength, num_reads=numruns)

    return sample_set


## ------- Main program -------
if __name__ == "__main__":

    ## ------- Set up our list of numbers -------
    S = [25, 7, 13, 31, 42, 17, 21, 10]

    # TODO: Enter your token here
    token = 'Your-Token-Here'

    ## ------- Set up our QUBO dictionary -------

    Q = define_QUBO(S)

    ## ------- Run our QUBO on the QPU -------

    sampler = EmbeddingComposite(DWaveSampler(endpoint='https://cloud.dwavesys.com/sapi/', token=token, solver={'qpu': True}))

    sample_set = run_on_QPU(Q, sampler)

    ## ------- Return results to user -------
    for sample in sample_set:
        S1 = [S[i] for i in sample if sample[i] == 1]
        S0 = [S[i] for i in sample if sample[i] == 0]
        print("S0 Sum: ", sum(S0), "\tS1 Sum: ", sum(S1), "\t", S0)