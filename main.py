from particle import *
from particle_updater import *
from particle_plotter import *


p = Particle(64, 2)
ParticleRandomInitializer.update(p)
p_updater = LangevinUpdater
p_updater.set_dt(0.1)
p_plotter = ParticlePlotter(p, p_updater)
p_plotter.run()
