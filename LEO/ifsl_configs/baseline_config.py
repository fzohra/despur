class Config():
    def __init__(self):
        self.is_config = True

def mini_5_resnet_baseline():
    config = Config()
    config.shot = 5
    config.test = True
    config.debug = False
    config.dataset = "miniImagenet"
    config.method = "simpleshot"
    config.model = "ResNet10"
    config.deconfound = False
    config.meta_label = "baseline"


    config.informative_features = 0
    config.informative_features_with_thresholding = False
    config.latent_features = False
    config.latents_threshold = None

    config.despur = False
    config.l_splits = 1
    config.corr_penalty = 0.01
    config.adapt_by_largest_loss = False
    config.regularize_mse = False
    config.regularize_kl = False
    config.zero_adjust = False
    config.key = "Hessians"

    return config

def mini_1_resnet_baseline():
    config = Config()
    config.shot = 1
    config.test = True
    config.debug = False
    config.dataset = "miniImagenet"
    config.method = "simpleshot"
    config.model = "ResNet10"
    config.deconfound = False
    config.meta_label = "baseline"

    config.informative_features = 0
    config.informative_features_with_thresholding = False
    config.latent_features = False
    config.latents_threshold = None

    config.despur = False
    config.l_splits = 1
    config.corr_penalty = 0.01
    config.adapt_by_largest_loss = False
    config.regularize_mse = False
    config.regularize_kl = False
    config.zero_adjust = False
    config.key = "Hessians"
    return config

def mini_5_wrn_baseline():
    config = Config()
    config.shot = 5
    config.test = True
    config.debug = False
    config.dataset = "miniImagenet"
    config.method = "simpleshotwide"
    config.model = "wideres"
    config.deconfound = False
    config.meta_label = "baseline"
    return config

def mini_1_wrn_baseline():
    config = Config()
    config.shot = 1
    config.test = True
    config.debug = False
    config.dataset = "miniImagenet"
    config.method = "simpleshotwide"
    config.model = "wideres"
    config.deconfound = False
    config.meta_label = "baseline"
    return config

def tiered_5_resnet_baseline():
    config = Config()
    config.shot = 5
    config.test = True
    config.debug = False
    config.dataset = "tiered"
    config.method = "simpleshot"
    config.model = "ResNet10"
    config.deconfound = False
    config.meta_label = "baseline"
    config.num_classes = 351
    return config

def tiered_1_resnet_baseline():
    config = Config()
    config.shot = 1
    config.test = True
    config.debug = False
    config.dataset = "tiered"
    config.method = "simpleshot"
    config.model = "ResNet10"
    config.deconfound = False
    config.meta_label = "baseline"
    return config

def tiered_5_wrn_baseline():
    config = Config()
    config.shot = 5
    config.test = True
    config.debug = False
    config.dataset = "tiered"
    config.method = "simpleshotwide"
    config.model = "wideres"
    config.deconfound = False
    config.meta_label = "baseline"
    config.num_classes = 351
    return config

def tiered_1_wrn_baseline():
    config = Config()
    config.shot = 1
    config.test = True
    config.debug = False
    config.dataset = "tiered"
    config.method = "simpleshotwide"
    config.model = "wideres"
    config.deconfound = False
    config.meta_label = "baseline"
    return config