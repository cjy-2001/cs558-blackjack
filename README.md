# CS 558 Blackjack Simulation

This repository contains a Python simulation for a simplified version of blackjack, designed as a solution for Problem Set 1 in the CS 558 course. The simulation includes an automated player that makes decisions based on a Monte Carlo simulation of blackjack strategies.

## Project Structure

The project is structured as follows:

- `card.py`: Defines the `Card` class, which represents a playing card with suit and rank.
- `config.py`: Contains global variables such as suits, ranks, and card values.
- `deck.py`: Defines the `Deck` class, which represents a deck of playing cards.
- `hand.py`: Defines the `Hand` class, which represents a player's hand in the game.
- `player.py`: Contains the `Player` class with methods to simulate blackjack strategies, play games, and report results.
- `player_draft.py`: An alternative or draft implementation of the `Player` class.

## Installation

To run this simulation, you need Python 3 installed on your system. Clone the repository to your local machine, navigate to the cloned directory, and you are ready to run the simulation.

```bash
git clone [repository-url]
cd cs558-blackjack
python player.py
```

## Function Descriptions
- sim(trials): Performs a Monte Carlo simulation to determine optimal playing strategies.
- hitme(playerhand, dealerfacecard): Determines whether the player should hit based on the hand value and dealer's face card.
- play(trials): Plays out a specified number of hands and returns the overall winning percentage.
- print_matrix(): Outputs the results of the simulation in a matrix format.

## Simulation Results

After running at least 100,000 hands, the simulation will provide a matrix of win/loss probabilities and the player's overall winning percentage. These results are based on the optimal strategies determined through the Monte Carlo simulation.