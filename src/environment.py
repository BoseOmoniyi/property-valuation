"""
Document and verify environment for reproducibility
"""
import sys
import platform

def print_environment_info():
    """Print complete environment information."""
    print("=" * 60)
    print("ENVIRONMENT INFORMATION")
    print("=" * 60)
    
    print(f"\nPython Version: {sys.version}")
    print(f"Platform: {platform.platform()}")
    
    print("\nInstalled Package Versions:")
    
    packages = [
        'pandas', 'numpy', 'scikit-learn', 
        'matplotlib', 'seaborn', 'requests', 'xgboost'
    ]
    
    for package_name in packages:
        try:
            package = __import__(package_name)
            version = package.__version__
            print(f"  {package_name:20s} {version}")
        except (ImportError, AttributeError):
            print(f"  {package_name:20s} NOT INSTALLED")
    
    print("=" * 60)

if __name__ == "__main__":
    print_environment_info()
def print_config_info():
    """Print all configuration parameters."""
    from config import *
    
    print("=" * 60)
    print("MODEL CONFIGURATION PARAMETERS")
    print("=" * 60)
    
    print("\n🔄 REPRODUCIBILITY")
    print(f"  Random State: {RANDOM_STATE}")
    
    print("\n🌐 API CONFIGURATION")
    print(f"  API URL: {WINNIPEG_API_URL}")
    print(f"  Dataset ID: {WINNIPEG_DATASET_ID}")
    
    print("\n🔧 DATA PROCESSING")
    print(f"  Test Size: {TEST_SIZE} ({int(TEST_SIZE*100)}%)")
    print(f"  Missing Threshold: {MISSING_THRESHOLD}")
    
    print("\n📊 MODEL FEATURES")
    print(f"  Target: {TARGET_VARIABLE}")
    print(f"  Features: {', '.join(BASELINE_FEATURES)}")
    
    print("\n🌲 RANDOM FOREST PARAMETERS")
    for param, value in RANDOM_FOREST_PARAMS.items():
        print(f"  {param}: {value}")
    
    print("\n✅ CROSS-VALIDATION")
    print(f"  Folds: {CV_FOLDS}")
    print(f"  Scoring: {CV_SCORING}")
    
    print("=" * 60)