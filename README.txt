This program is a text-based version of a casino table game by the same name. It was fun when I played it and I thought it’d be a good way to practice programming. It is essentially a heads-up game of Texas Holdem against the dealer. The house edge comes in the payout - the house pays out 1-to-1 on all bets EXCEPT the ante, unless the player has a straight or higher in which case the house pays to the ante as well.

The gameplay is as follows:

1)  The player chooses an ante amount, $5 or higher. All future bets will be tied to the initial ante amount.

2)  Two cards are dealt, just as in Texas Holdem poker. Based on these two cards, the player decides if they would like to see the flop or fold. Seeing the flop requires a bet of twice the ante amount, but after that the player may stay in for the remaining cards for free.

3)  The flop is dealt. Based on their current hand, the player decides if they would like to bet further or check and see the next card for free.

4)  The turn is dealt. Based on their current hand, the player decides if they would like to bet further or check and see the last card for free.

5)  The river is dealt, and the dealer is given his two cards. The hands are then compared, and the player is either paid or his bets are taken off the table.

There is a lot I could add as I learn more, such as an actual GUI for the game, or saving progress so that players can keep track of their winnings over time.

Enjoy, and feel free to rip my code to shreds, since I’m sure it’s not particularly “Pythonic” or proper or anything - I need to learn!