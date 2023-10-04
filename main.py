import pygame, random, math
import pymunk.pygame_util
from settings import *
from utils import generate_new_food, generate_physic_frame
from producer import Produser
from typing import List
import csv


produsers_nums: List[int] = []


class World:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW.x, WINDOW.y))
        self.screen.fill(GREY_34)
        self.clock = pygame.time.Clock()
        self.time = 0

        pymunk.pygame_util.positive_y_is_up = False
        self.draw_options = pymunk.pygame_util.DrawOptions(self.screen)
        self.space = pymunk.Space()
        self.space.gravity = 0, 0

        # self.fig = plt.figure()
        # self.ax = self.fig.add_subplot(1, 1, 1)

        generate_physic_frame(self.space)

        self.world = {"prodisers": []}

        self.produsers: List[Produser] = []

        for i in range(50):
            self.produsers.append(
                Produser(
                    physic_space=self.space,
                    position=(random.randint(0, WINDOW.x), random.randint(0, WINDOW.y)),
                    size=produsers_base_size,
                    mass=produsers_base_mass,
                    energy=random.randint(0, produsers_max_energy),
                )
            )
        # X = deque(maxlen = 20)
        # X.append(1)

        # Y = deque(maxlen = 20)
        # Y.append(1)

        # self.app = dash.Dash(__name__)

        # self.app.layout = html.Div(
        #     [
        #         dcc.Graph(id = 'live-graph', animate = True),
        #         dcc.Interval(
        #             id = 'graph-update',
        #             interval = 1000,
        #             n_intervals = 0
        #         ),
        #     ]
        # )

        # @self.app.callback(
        #     Output('live-graph', 'figure'),
        #     [ Input('graph-update', 'n_intervals') ]
        # )

        # def update_graph_scatter(n):
        #     X.append(X[-1]+1)
        #     Y.append(Y[-1]+Y[-1] * random.uniform(-0.1,0.1))

        #     data = plotly.graph_objs.Scatter(
        #             x=list(X),
        #             y=list(Y),
        #             name='Scatter',
        #             mode= 'lines+markers'
        #     )

        #     return {'data': [data],
        #             'layout' : go.Layout(xaxis=dict(range=[min(X),max(X)]),yaxis = dict(range = [min(Y),max(Y)]),)}

        # # app.run_server()

    # def animate(self, i):
    #     xs = []
    #     ys = []

    #     # for produser_index, produser in enumerate(self.produsers):
    #     #     xs.append(float(i))
    #     #     ys.append(float(len(self.produsers)))

    #     self.ax.clear()
    #     self.ax.plot(xs, ys)

    #     plt.xlabel("Название")
    #     plt.ylabel("Цена")
    #     plt.title("График обновляемый в режиме реального времени")

    def run(self):
        while True:
            delta = self.clock.tick(FPS)
            self.screen.fill(GREY_34)
            self.time += delta

            if self.time >= 500:
                self.time = 0
                produsers_nums.append(len(self.produsers))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return ()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return ()
            # physic
            for produser in self.produsers:
                produser.update(delta, produsers=self.produsers, space=self.space)
                color = GREEN
                color += pygame.Color(0, produser.energy, 0)
                pygame.draw.circle(
                    self.screen, color, produser.body.body.position, produser.body.size
                )

            self.space.step(1 / FPS)
            # space.debug_draw(draw_options)

            pygame.display.set_caption("FPS: " + str(int(self.clock.get_fps())))
            pygame.display.flip()


world = World()
world.run()

with open("results.csv", "w", newline="") as f:
    # creating the writer
    writer = csv.writer(f)
    # using writerows, all rows at once
    Our_list = [
        ["parametr", "value"],
        *[[str(i), produsers_nums[i]] for i in range(len(produsers_nums))],
    ]
    writer.writerows(Our_list)
