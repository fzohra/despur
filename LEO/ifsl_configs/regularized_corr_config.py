class Config():
    def __init__(self):
        self.is_config = True

def mini_5_resnet_latents_split_8_0():
    config = mini_5_resnet_baseline_reg()
    config.despur = True
    config.l_splits = 8
    config.corr_penalty = 1.0
    return config

def mini_5_resnet_latents_split_8_1():
    config = mini_5_resnet_baseline_reg()
    config.despur = True
    config.l_splits = 8
    config.corr_penalty = 0.1
    return config

def mini_5_resnet_latents_split_8_2():
    config = mini_5_resnet_baseline_reg()
    config.despur = True
    config.l_splits = 8
    config.corr_penalty = 0.01
    return config

def mini_5_resnet_latents_split_8_3():
    config = mini_5_resnet_baseline_reg()
    config.despur = True
    config.l_splits = 8
    config.corr_penalty = 0.001
    return config

def mini_5_resnet_baseline_reg():
    config = Config()
    config.shot = 5
    config.test = True
    config.debug = False
    config.dataset = "miniImagenet"
    config.method = "simpleshot"
    config.model = "ResNet10"
    config.deconfound = False
    config.meta_label = "baseline"
    return config

def mini_1_resnet_baseline_reg():
    config = Config()
    config.shot = 1
    config.test = True
    config.debug = False
    config.dataset = "miniImagenet"
    config.method = "simpleshot"
    config.model = "ResNet10"
    config.deconfound = False
    config.meta_label = "baseline"
    return config
