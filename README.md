# InfiniteMonkeyChallenge
<!-- toc -->

 - [Motivation](#motivation)
 - [Installation Instructions](#installation-instructions)
 - [Expected Time to Complete Challenge](#expected-time-to-complete-challenge)
 - [Next Steps](#next-steps)

<!-- tocstop -->

## Motivation
How long will it take for random typing to recreate one of Shakespeare's greatest works?
|![Monkey with a typewriter](https://upload.wikimedia.org/wikipedia/commons/3/3c/Chimpanzee_seated_at_typewriter.jpg)|
|:-:|
|From [Wikipedia](https://en.wikipedia.org/wiki/Infinite_monkey/theorem)|

[The Infinite Monkey Theorem](https://en.wikipedia.org/wiki/Infinite_monkey_theorem) is famous for its profound __ on the concept of infinity, despite its ridiculous premise.
It states that given enough time, a monkey randomly typing characters will at some point recreate the complete works of Shakespeare.
Furthermore, the monkey will recreate any finite length text. Of course, the odds of this happening are extremely low (discussed in [Expected Time to Complete Challenge](#expected-time-to-complete-challenge)).
The goal of this project is to simulate random typing (at least as well as python's random library allows us to) and see if our "monkey" gets really really really lucky in recreating Shakespeare's works.

## Installation Instructions
1. Install [Python](https://www.python.org/downloads/)
2. Clone repo onto local machine
3. Install dependencies using `pip install -r requirements.txt` 
4. Run `python main.py` in the src folder
5. If you want to see an easier challenge of typing out the alphabet, include the `-t` or `--test` flag when running the command in step 3.
6. Similarly, if you want intermediate results to be printed, include the `-pi` or `--print_intermediate` flag when running step 3.

## Expected Time to Complete Challenge
You can find a variety of expected times to recreate Shakespeare with random typing.
In this project, a random character is chosen from a set of 83 characters, based on the characters found in Project Gutenberg's "The Complete Works of William Shakespeare by William Shakespeare."
The length of the entire works is 4,880,671 characters.
If we assume that each character is chosen independently with uniform probability, then the probability of completing the challenge is 1/(83^4,880,671).
I couldn't even find a calculator capable of calculating that number, which goes to show how absurdly small the chance is of completing this challenge.
But it'll still be fun to see how far it gets!

I've included an easier challenge of randomly typing out the alphabet.
We allow the simulation to type any of the 26 lower case characters in the English alphabet.
The length of the alphabet is 26, so the probability of success is 1/(26^26), or roughly 1.6e-37.
Still not great odds, but a little belief goes a long way!

## Next Steps
In its current state, the project is an interactive CLI app that runs the simulation for a number of time steps specified by the user.
However, I'd ideally like to let the simulation run indefinitely and see how far it could get.
To do so, I'm going to next work on deploying the simulation as a website that constantly runs the simulation on the back end and displays current progress and best results to visitors.
I'll have separate instances of the simulation working on a number of challenges with varying difficulty.
