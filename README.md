# cs558-blackjack
CS 458/558 - Problem Set 1 (blackjack)

This program implements a pretty vanilla form of blackjack. You cannot double down, buy insurance, or count cards. There is one deck and it is reshuffled before every hand. The dealer has no discretion. She has to stay on 17 or higher.

For this code, the human is in the loop. The player has to click the hit or stand buttons. Your job is to automate this process.

Create a function hitme(playerhand, dealerfacecard) which returns a boolean value, true or false, specifying whether the player should ask for another card or not. That is, after the cards are initially dealt, the program will call hitme and either ask for another card or stand - untouched by human hands.

Even though the example code uses graphics, your code should not. It should be built for speed, not looks.

The hitme function will simply perform a table look-up. You will have a 2 dimensional matrix comprising the optimal strategy for all possible combinations of player hands and dealer face cards. The values in the matrix will simply be true or false. For example,

hitme(12, 1) ==> true
If your hand value is 12 and the dealer has an ace, you should ask for another card.
hitme(18, 4) ==> false
If your hand value is 18 and the dealer shows a four, you should stay put.
Actually, it is not up to you to populate the values of the table through dint of insight. Rather, you will write another function sim(trials), which performs Monte Carlo simulation.

The sim function will perform a boatload of trials and produce as output a matrix of probabilities. For example, in the cell corresponding to a player hand of 18 and a dealer face card of 4, the value may be 235 / 978 meaning that this combination occurred 978 times in the simulation and in only 235 times did the player win if she asked for another card. You would then convert that matrix to boolean values, based on some threshold ratio value. The normal approach would be to use 50%, but you may decide to use a different value.

Once you have your hitme table installed, run your own simulated games, keeping track of the win/loss ratio. Report your results for simulations of at least 100,000 hands.

Finally, write a function play(trials) which will play the given number of hands and return your overall winning percentage.

You should submit one file: player.py In addition, you should hand in a README file which explains what function does what, as well as a transcript including the output of Monte Carlo simulation, and the summary output of 100,000 game playing trials - how many games the player won. In the past when giving assignments involving automated game playing, I have awarded a prize to the most successful program. Keep that in mind.

The process for creating this program is similar to most large scale decision systems: caching the results of a massive simulation that can enable rapid, real time decisions.