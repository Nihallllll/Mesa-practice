import mesa
import matplotlib.pyplot as plt

# --- 2. THE AGENT (The Toy) ---
class CookieEater(mesa.Agent):
    def __init__(self, model):
        super().__init__(model)
        self.energy = 10 

    def move(self):
        # 4. THE SPACE: Looking at the neighbors on the grid
        possible_steps = self.model.grid.get_neighborhood(self.pos, moore=True, include_center=False)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

    def eat(self):
        # 6. PROPERTY LAYER: Looking at the "Sticker Map" for crumbs
        x, y = self.pos
        crumbs_here = self.model.grid.properties["crumbs"].data[x, y]
        
        if crumbs_here > 0:
            # 10. USER PARAMETERS: Using the "cookie_value" knob
            self.energy += self.model.cookie_value
            self.model.grid.properties["crumbs"].set_cell((x, y), 0)

    # 3. THE STEP: What the agent does when the clock ticks
    def step(self):
        self.move()
        self.eat()
        self.energy -= 1 
        if self.energy <= 0:
            self.remove()

# --- 1. THE MODEL (The Big Box) ---
class CookieWorld(mesa.Model):
    def __init__(self, n_eaters=20, width=10, height=10, cookie_value=5, seed=None):
        super().__init__(seed=seed)
        self.cookie_value = cookie_value
        
        # 4. THE SPACE: The playground floor
        self.grid = mesa.space.MultiGrid(width, height, torus=True)
        
        # 6. PROPERTY LAYER: Making the "Invisible Cookie Map"
        crumb_layer = mesa.space.PropertyLayer("crumbs", width, height, default_value=1)
        self.grid.add_property_layer(crumb_layer)

        # Creating the agents
        for i in range(n_eaters):
            eater = CookieEater(self)
            x = self.random.randrange(width)
            y = self.random.randrange(height)
            self.grid.place_agent(eater, (x, y))

        # 7. DATA COLLECTOR: The Secret Notebook
        self.datacollector = mesa.DataCollector(
            model_reporters={"Eaters_Left": lambda m: len(m.agents)}
        )

    # 3. THE STEP: What the world does when the clock ticks
    def step(self):
        # 5. AGENTSET: Picking up the "Bag of Toys" and telling them to play
        self.agents.shuffle_do("step")
        
        # Every turn, one new cookie appears (Regrowth)
        rx = self.random.randrange(self.grid.width)
        ry = self.random.randrange(self.grid.height)
        self.grid.properties["crumbs"].set_cell((rx, ry), 1)
        
        # Write down the results in the notebook
        self.datacollector.collect(self)

# --- 10. USER PARAMETERS: Turning the knobs before we start ---
my_world = CookieWorld(n_eaters=40, cookie_value=8)

# Running the game for 30 "Ticks"
for i in range(30):
    my_world.step()

# --- 9. VISUALIZATION: Turning the notebook into a TV picture (Chart) ---
stats = my_world.datacollector.get_model_vars_dataframe()
stats.plot(title="The Survival Story of Cookie Eaters")
plt.xlabel("Time (Steps)")
plt.ylabel("Number of Eaters")
plt.show()

# --- 8. BATCHRUNNER: The "What If?" Machine ---
# This part is for running many worlds at once (optional)
print("If you want to run many games at once, use mesa.batch_run!")