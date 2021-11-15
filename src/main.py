# Contains an interactive CLI app that runs the simulation a user-specified number of times
# Updates user on progress of the simulation as well as best progress so far
from simulator import Simulator
from trie import create_trie
import argparse

def test_setup() -> Simulator:
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    works = [alphabet]
    valid_chars = alphabet 
    
    trie = create_trie(works)
    simulator = Simulator(trie, valid_chars)
    
    return simulator

def setup() -> Simulator:
    # get works
    works_path = '../data/works/'
    works = []
    for i in range(182):
        with open(works_path + f'{i}.txt') as f:
            works.append(f.read())

    # get valid chars
    with open('../data/valid_chars.txt') as f:
        valid_chars = f.read()

    # build trie
    trie = create_trie(works)

    # init simulator
    simulator = Simulator(trie, valid_chars)

    return simulator

def run_simulation(simulator: Simulator, answer: int, should_print: bool) -> tuple[int, int]:
    best_over_run = 0
    for _ in range(answer):
        next_letter, curr_percentage = simulator.next()

        if should_print:
            if len(simulator.get_current_string()) > 0:
                print(simulator.get_current_string())
            else:
                print(next_letter)

        if next_letter is None:
            return node, 100, 100
        best_over_run = max(best_over_run, curr_percentage)

    return simulator.get_current_percentage(), best_over_run

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--test', help='enable if you want to run simulation on smaller works (alphabet)', action='store_true')
    parser.add_argument('-pi', '--print_intermediate', help='enable if every simulation result should be printed (besides mistakes)', action='store_true')
    args = parser.parse_args()
    if args.test:
        simulator = test_setup()
    else:
        simulator = setup()

    curr_percentage = best_percentage = simulator.get_current_percentage()

    while True:
        answer = input('Insert number of characters to generate or "quit" to end simulation:\n')
        if answer == 'quit':
            print(f'Best percentage: {best_percentage}%')
            break

        try:
            # don't want to just directly convert to int b/c floats will just be silently truncated
            answer = float(answer)
        except ValueError:
            print('Invalid input')
            continue

        # check if answer has decimals
        if answer % 1 != 0:
            print('Invalid input')
            continue

        answer = int(answer)

        # run simulation
        curr_percentage, best_percent_over_run = run_simulation(simulator, answer, args.print_intermediate)
        best_percentage = max(best_percentage, best_percent_over_run)

        if best_percentage == 100:
            print('Challenge Complete!')
            break
        
        print(f'Current Progress: {curr_percentage}%')
        print(f'Best During Last Run: {best_percent_over_run}%')
        print(f'All-time highest: {best_percentage}%')
        
