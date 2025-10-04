"""
Ensure reproducibility across all random operations
"""
import random
import numpy as np
import os

def set_random_seeds(seed=42):
    """
    Set random seeds for reproducibility.
    
    Parameters
    ----------
    seed : int, default=42
        Random seed value
    """
    # Python's built-in random
    random.seed(seed)
    
    # Numpy
    np.random.seed(seed)
    
    # Python hash seed (for dictionary ordering, etc.)
    os.environ['PYTHONHASHSEED'] = str(seed)
    
    print(f"✓ Random seeds set to {seed} for reproducibility")

if __name__ == "__main__":
    set_random_seeds(42)