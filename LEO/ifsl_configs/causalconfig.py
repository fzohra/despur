class Config():
    def __init__(self):
        self.is_config = True

def mini_5_resnet_latents_causal_0():
    config = mini_5_resnet_ifsl_causal()
    config.preprocess_before_split = "hl2n"
    config.preprocess_after_split = "l2n"
    config.key = "A"
    return config

def mini_5_resnet_latents_causal_1():
    config = mini_5_resnet_ifsl_causal()
    config.preprocess_before_split = "hl2n"
    config.preprocess_after_split = "l2n"
    config.informative_features = 3
    config.key = "BFinal"
    #best acc: 0.7459208726882934 best dacc: 0.7111537158489227
    return config

def mini_5_resnet_latents_causal_2():
    config = mini_5_resnet_ifsl_causal()
    config.preprocess_before_split = "hl2n"
    config.preprocess_after_split = "l2n"
    config.informative_features = 2
    config.key = "CFinal"

    return config

def mini_5_resnet_latents_causal_3():
    config = mini_5_resnet_ifsl_causal()
    config.preprocess_before_split = "cl2n"
    config.preprocess_after_split = "l2n"
    config.informative_features = 3
    config.informative_features_with_thresholding = True
    config.fusion ="concat"
    config.key = "D"

    return config

def mini_5_resnet_latents_causal_4():
    config = mini_5_resnet_ifsl_causal()
    config.preprocess_before_split = "cl2n"
    config.preprocess_after_split = "l2n"
    config.informative_features = 3
    config.informative_features_with_thresholding = True
    config.key = "E"

    return config

def mini_5_resnet_latents_causal_5():
    config = mini_5_resnet_ifsl_causal()
    config.l_splits = 4
    config.corr_penalty = 0.001

    config.preprocess_before_split = "cl2n"
    config.preprocess_after_split = "l2n"
    config.latent_features = True
    config.key = "F"

    return config

def mini_5_resnet_latents_causal_6():
    config = mini_5_resnet_ifsl_causal()
    config.l_splits = 4
    config.corr_penalty = 0.001

    config.preprocess_before_split = "cl2n"
    config.preprocess_after_split = "l2n"
    config.latent_features = True
    config.latents_threshold = 1e-3
    config.key = "G"

    return config

def mini_5_resnet_latents_causal_7():
    config = mini_5_resnet_ifsl_causal()
    config.despur = True
    config.l_splits = 8
    config.corr_penalty = 0.001
    config.adapt_by_largest_loss = True
    config.regularize_mse = False
    config.regularize_kl = False
    config.key = "H"

    return config

def mini_5_resnet_latents_causal_8():
    config = mini_5_resnet_ifsl_causal()
    config.despur = True
    config.l_splits = 2
    config.corr_penalty = 0.466387
    config.adapt_by_largest_loss = True
    config.regularize_mse = True
    config.regularize_kl = False
    config.key = "I"

    return config

def mini_5_resnet_latents_causal_9():
    config = mini_5_resnet_ifsl_causal()
    config.despur = True
    config.l_splits = 2
    config.corr_penalty = 0.0001
    config.adapt_by_largest_loss = True
    config.regularize_mse = True
    config.regularize_kl = False
    config.key = "J"

    return config

def mini_5_resnet_ifsl_causal():
    config = Config()
    config.shot = 5
    config.test = True
    config.debug = False
    config.dataset = "miniImagenet"
    config.method = "simpleshot"
    config.model = "ResNet10"
    config.deconfound = True
    config.meta_label = "ifsl"
    # IFSL parameters
    config.n_splits = 8 #1
    config.fusion = "+"
    config.classifier = "single"
    config.num_classes = 64
    config.logit_fusion = "product"
    config.use_x_only = False
    config.preprocess_before_split = "cl2n"
    config.preprocess_after_split = "l2n"
    config.is_cosine_feature = True
    config.normalize_before_center = True
    config.normalize_d = False
    config.normalize_ed = False
    # config.outer_lr = 1.51024e-4

    config.despur = False
    config.l_splits = 5
    config.corr_penalty = 0.001
    config.adapt_by_largest_loss = False
    config.regularize_mse = False
    config.regularize_kl = False

    config.informative_features = 0
    config.informative_features_with_thresholding = False
    config.latent_features = False
    config.latents_threshold = None
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
