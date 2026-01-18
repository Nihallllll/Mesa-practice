Mesa is like a giant digital toy box that lets you build your own tiny worlds with little people (or animals, or cells) inside them to see how they behave.

Here is a list of all the main concepts in Mesa, explained like you are three years old!

1. The Model (The "Big World")
Code name: mesa.Model The Model is like the big cardboard box that holds your entire game. It’s the "boss" of the world. It keeps track of the rules, the time, and everyone living inside it. Without the box, your toys would just be rolling around on the floor!

2. The Agent (The "Little Person")
Code name: mesa.Agent An Agent is like a little Lego person or a toy. Each one can have its own name, its own favorite color (data), and its own things it likes to do. One agent might want to find food, while another might just want to walk around.

3. The Step (The "Tick-Tock")
Code name: step() The Step is like a giant clock saying "Go!" Every time the clock ticks, everyone in the world gets a turn to move or do something. When the clock stops, the game pauses.

4. The Space (The "Playground")
Code name: mesa.space This is where the little people live. There are different kinds of playgrounds:

Grid (The Checkerboard): Everyone sits in a square, like on a chess board.

Continuous Space (The Big Room): You can stand anywhere you want, not just in a square!

Network (The Spider Web): Everyone is connected by strings, and you can only visit people you are connected to.

5. The AgentSet (The "Magic Team")
Code name: AgentSet Imagine you have a big bag of marbles. An AgentSet is that bag! It has special powers:

You can say, "All the red marbles, hop!" (select)

You can shake the bag so they move in a random order (shuffle).

You can tell everyone in the bag to do their homework at the same time (do).

6. Property Layers (The "Sticker Maps")
Code name: PropertyLayer Imagine your playground has a special map on the floor. Some parts are "Hot" and some are "Cold." A Property Layer is like a giant sticker you put over the whole board that tells the agents something about where they are standing, like how much grass is there to eat.

7. The DataCollector (The "Secret Notebook")
Code name: mesa.DataCollector While you play, a robot stands next to you with a notebook. Every time the clock ticks, the DataCollector writes down how many people are happy or how many toys are left. Later, you can look at the notebook to see a pretty picture (a graph) of what happened.

8. The BatchRunner (The "What If?" Machine)
Code name: batch_run This is like having a superpower to play the same game 100 times very, very fast! You can change one rule (like "What if everyone had two cookies instead of one?") and see how the world changes each time.

9. Visualization (The "TV Screen")
Code name: SolaraViz This is the TV that shows you what is happening inside the computer. Instead of just looking at boring numbers, you see the little dots moving, changing colors, and interacting on your screen.

10. User Parameters (The "Knobs and Sliders")
Code name: UserParam / Slider These are like the knobs on a radio. You can slide them left or right to change the game while it’s running—like making it rain more or adding more toy people to the box.

How the Pages Connect (The "Map")
If you were to walk through the documentation links, here is how you would go deeper:

Home Page: Tells you what Mesa is.

Getting Started: Shows you how to open the toy box.

Tutorials: Teaches you how to build your first Lego person (Agent) and world (Model).

API Docs (The Deepest Part): This is the "Instruction Manual" for every single tiny piece. It explains:

mesa.model: How to build the box.

mesa.agent: How to build the people.

mesa.space: How to draw the floor.

mesa.datacollection: How to use the notebook.

mesa.visualization: How to turn on the TV.