# config.py

# configuration for game
game = dict(
    stage_width         = 85.5656967163086, # HALF the stage width of FINAL DESTINATION
    g_time              = 4000, # game time
    t_time              = 4000, # game testing time
    fps                 = 60, # frame per second
    delay               = 20, # terminal update delay
    n_best              = 5, # number of best agents
    n_agents            = 30, # number of agents
)

nnet = dict(
    n_inputs    = 19,
    n_h_neurons = 30,
    n_outputs   = 14,
    n_weights   = (19+1) * (30) + (30+1) * (14), # (inputs + bias) * (h_neurons) + (h_neurons + bias) * (outputs)
)