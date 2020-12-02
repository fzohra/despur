class Config():
    def __init__(self):
        self.is_config = True

def mini_5_resnet_latents_split_8_0():
    config = mini_5_resnet_baseline_reg()
    config.despur = True
    config.l_splits = 8
    config.corr_penalty = 0.001
    config.adapt_by_largest_loss = True
    config.regularize_mse = True
    config.regularize_kl = False
    return config

def mini_5_resnet_latents_split_8_1():
    config = mini_5_resnet_baseline_reg()
    config.despur = True
    config.l_splits = 4
    config.corr_penalty = 0.001
    config.adapt_by_largest_loss = True
    config.regularize_mse = True
    config.regularize_kl = False
    return config

def mini_5_resnet_latents_split_8_2():
    config = mini_5_resnet_baseline_reg()
    config.despur = True
    config.l_splits = 2
    config.corr_penalty = 0.001
    config.adapt_by_largest_loss = True
    config.regularize_mse = True
    config.regularize_kl = False
    return config

def mini_5_resnet_latents_split_8_3():
    config = mini_5_resnet_baseline_reg()
    config.despur = True
    config.l_splits = 1
    config.corr_penalty = 0.001
    config.adapt_by_largest_loss = True
    config.regularize_mse = True
    config.regularize_kl = False
    return config

def mini_5_resnet_latents_split_8_4():
    config = mini_5_resnet_baseline_reg()
    config.despur = True
    config.l_splits = 1
    config.corr_penalty = 0.001
    config.adapt_by_largest_loss = True
    config.regularize_mse = False
    config.regularize_kl = False
    return config

def mini_5_resnet_latents_split_8_5():
    config = mini_5_resnet_baseline_reg()
    config.despur = True
    config.l_splits = 2
    config.corr_penalty = 0.001
    config.adapt_by_largest_loss = True
    config.regularize_mse = False
    config.regularize_kl = False
    return config

def mini_5_resnet_latents_split_8_6():
    config = mini_5_resnet_baseline_reg()
    config.despur = True
    config.l_splits = 4
    config.corr_penalty = 0.001
    config.adapt_by_largest_loss = True
    config.regularize_mse = False
    config.regularize_kl = False
    return config

def mini_5_resnet_latents_split_8_7():
    config = mini_5_resnet_baseline_reg()
    config.despur = True
    config.l_splits = 8
    config.corr_penalty = 0.001
    config.adapt_by_largest_loss = True
    config.regularize_mse = False
    config.regularize_kl = False
    return config

def mini_5_resnet_latents_split_8_8():
    config = mini_5_resnet_baseline_reg()
    config.despur = True
    config.l_splits = 2
    config.corr_penalty = 0.466387
    config.adapt_by_largest_loss = True
    config.regularize_mse = True
    config.regularize_kl = False
    return config

def mini_5_resnet_latents_split_8_9():
    config = mini_5_resnet_baseline_reg()
    config.despur = True
    config.l_splits = 2
    config.corr_penalty = 0.466387
    config.adapt_by_largest_loss = True
    config.regularize_mse = False
    config.regularize_kl = False
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
    config.meta_label = "despur"
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
    config.meta_label = "despur"
    return config
