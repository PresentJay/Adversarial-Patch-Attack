import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import pickle
import traceback
from src import configs, datasets, models, patches
from utils import imgUtil, logUtil

def patch_validator():
    # load the Network Settings
    args = configs.Initialization()
    
    log = logUtil.log(args.resultdir, args.log_type)
    log.write(f'Random Seed: {args.seed}', _print=True)
    log.write(f'rotation: {args.min_rotation}-{args.max_rotation} degree', _print=True)
    log.write(f'scale: {args.min_scale*100}%-{args.max_scale*100}%', _print=True)
    EOT_FACTORS = {
        "scale" : (args.min_scale, args.max_scale),
        "rotation": (args.min_rotation, args.max_rotation)
    }
    try:
        log.write(f'start validate patches with {args.iter_val} data iterations of validation set', _print=True)
        patch.measure_attackCapability(classifier=classifier, eot_dict=EOT_FACTORS, iteration=args.iter_val)
        log.write(f'Randomly patched model {classifier.getName()} has {patch.attackedAccuracy:.2f}% of accuracy to original, ', end='', _print=True)
        log.write(f'and {patch.attackCapability:.2f}% of accuracy to target {args.target_class}', _print=True)
        
        log.save()
        with open(args.resultdir + "/patch.pkl", "wb") as f:
            pickle.dump(patch.data.cpu(), f)
    except Exception as e:
        log.write(f'error occured during validating')
        with open(args.resultdir + "/patch.pkl", "wb") as f:
            pickle.dump(patch.data.cpu(), f)
        log.save()
        