# Functions

- should_hit function determines whether the player should hit based on the player's current hand value, the dealer's visible card value, and historical win rates stored in the strategy matrix. After collecting enough data, the function uses a threshold win rate (THRESHOLD_WIN_RATE) to decide if hitting has historically led to winning outcomes in similar situations.

- dealer_turn simulates the dealer's turn, where the dealer keeps drawing cards from the deck until the hand value is at least 17. This is in line with standard Blackjack dealer rules.

- compare_hands compares the final values of the player's and dealer's hands to determine the winner. It accounts for cases where either the player or the dealer busts (exceeds 21).

- sim conducts a simulation of Blackjack games for a specified number of trials to populate the strategy matrix with data. Each trial simulates a game where the player's decisions are made randomly, and the outcomes are used to update win rates in the strategy matrix.

- hitme decides whether to hit during an actual game based on the strategy matrix. This method is similar to should_hit but is used during the play method to make hit/stand decisions after the matrix has been populated with simulation data.

- play plays a specified number of games using the strategy learned from the simulation. It returns the win rate (the proportion of games won) based on decisions made using the strategy matrix.

- print_matrix prints the strategy matrix. Each cell shows the win rate for a specific player hand value against a dealer's face card value, providing insight into which decisions lead to the highest probability of winning.

Here is the result of the Monte Carlo simulation:

PS C:\Users\User\OneDrive - Yale University\Academic\Yale Academic\2024 Spring\CPSC 558\cs558-blackjack> py player.py
        1       2       3       4       5       6       7       8       9       10
4       17.78%  41.29%  44.14%  46.24%  48.86%  49.07%  37.49%  32.35%  30.19%  27.44%
5       16.66%  41.26%  43.12%  45.21%  49.77%  47.94%  35.10%  33.17%  29.05%  26.91%
6       15.38%  39.70%  42.26%  47.30%  49.75%  47.79%  34.70%  31.60%  28.75%  25.68%
7       16.60%  40.56%  42.66%  46.31%  49.04%  49.00%  36.43%  32.31%  29.47%  25.64%
8       20.20%  46.24%  47.60%  51.17%  53.59%  54.36%  47.13%  37.17%  33.23%  29.50%
9       24.22%  50.67%  52.83%  55.17%  57.62%  57.64%  52.78%  49.02%  39.08%  33.71%
10      30.52%  56.35%  58.50%  60.29%  62.56%  61.16%  57.30%  54.07%  49.76%  40.15%
11      34.86%  58.31%  60.94%  62.50%  64.62%  64.30%  58.78%  54.56%  52.23%  46.54%
12      17.93%  35.99%  36.91%  38.52%  39.72%  40.30%  34.52%  30.55%  27.69%  25.89%
13      17.40%  33.70%  35.44%  37.19%  37.90%  38.12%  33.19%  29.63%  29.08%  24.96%
14      16.65%  31.70%  31.89%  34.19%  34.93%  35.41%  31.46%  29.76%  27.34%  23.70%
15      15.59%  28.84%  29.46%  29.55%  32.63%  32.27%  31.37%  28.09%  25.56%  22.35%
16      15.56%  27.92%  28.09%  28.66%  28.91%  33.01%  30.23%  27.63%  25.07%  21.42%
17      14.69%  25.32%  25.38%  25.89%  28.21%  27.54%  29.96%  26.60%  23.64%  20.37%
18      13.42%  22.82%  23.11%  25.32%  25.85%  26.19%  25.45%  25.91%  22.24%  19.05%
19      11.05%  19.29%  21.18%  21.99%  22.38%  22.31%  22.86%  21.05%  21.24%  17.39%
20      6.23%   12.80%  12.99%  13.12%  13.58%  13.45%  13.08%  12.91%  11.75%  11.61%
21      0.00%   0.00%   0.00%   0.00%   0.00%   0.00%   0.00%   0.00%   0.00%   0.00%
0.424

After playing 100,000 games, the winning rate of the player is 0.424. That makes sense because in our case, the dealer is taking advantages.