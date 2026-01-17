import mesa
import pandas as pd
import matplotlib.pyplot as plt

# --- 1. THE AGENT (The Toy) ---
class CookieEater(mesa.Agent):
    def __init__(self, model):
        super().__init__(model)
        self.energy = 10 

    def move(self):
        # 3. THE SPACE: Find neighbors on the floor
        possible_steps = self.model.grid.get_neighborhood(self.pos, moore=True, include_center=False)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def eat(self):
        # 4. PROPERTY LAYER: Check the "Sticker Map" for crumbs
        x, y = self.pos
        # We look at the 'crumbs' layer we built in the Model
        crumbs_here = self.model.grid.properties["crumbs"].data[x, y]
        
        if crumbs_here > 0:
            self.energy += self.model.cookie_value
            # Clean up the crumb (set to 0)
            self.model.grid.properties["crumbs"].set_cell((x, y), 0)

    def step(self):
        # 2. THE STEP: Every turn, move and eat
        self.move()
        self.eat()
        self.energy -= 1 # Walking makes you hungry!
        if self.energy <= 0:
            self.remove() # Leave the game if no energy

# --- 5. THE MODEL (The Box) ---
class CookieWorld(mesa.Model):
    def __init__(self, n_eaters=20, width=10, height=10, cookie_value=5, seed=None):
        super().__init__(seed=seed)
        self.cookie_value = cookie_value
        
        # 3. THE SPACE: The classic checkerboard floor
        self.grid = mesa.space.MultiGrid(width, height, torus=True)
        
        # 4. PROPERTY LAYER: Create the "Crumb Map"
        # We make a layer named "crumbs" and fill it with 1s (cookies everywhere!)
        crumb_layer = mesa.space.PropertyLayer("crumbs", width, height, default_value=1)
        self.grid.add_property_layer(crumb_layer)

        # Put eaters in the box
        for i in range(n_eaters):
            eater = CookieEater(self)
            x = self.random.randrange(width)
            y = self.random.randrange(height)
            self.grid.place_agent(eater, (x, y))

        # 7. DATA COLLECTOR: The Secret Notebook
        self.datacollector = mesa.DataCollector(
            model_reporters={"Eaters_Left": lambda m: len(m.agents)}
        )

    def step(self):
        # 6. AGENTSET: Tell the whole "Bag of Toys" to move
        self.agents.shuffle_do("step")
        
        # Randomly drop a new cookie crumb on the floor
        rx = self.random.randrange(self.grid.width)
        ry = self.random.randrange(self.grid.height)
        self.grid.properties["crumbs"].set_cell((rx, ry), 1)
        
        self.datacollector.collect(self)

# --- 8. RUNNING THE MODEL ---
# 10. USER PARAMS: Change these to see what happens!
my_world = CookieWorld(n_eaters=30, cookie_value=10)

for i in range(25):
    my_world.step()

# --- 9. VISUALIZATION ---
# Look at our notebook and draw a picture
stats = my_world.datacollector.get_model_vars_dataframe()
stats.plot(title="How many eaters stayed full?")
plt.show()

# 9. BATCHRUNNER: Let the computer play many games for us
params = {
    "n_eaters": [10, 50, 100],  # What if we start with more people?
    "cookie_value": [2, 10],     # What if cookies are super yummy?
    "width": 10,
    "height": 10
}

results = mesa.batch_run(
    CookieWorld,
    params,
    iterations=5, # Play each version 5 times
    max_steps=30,
    data_collection_period=1
)

print("Finished playing all the games!")