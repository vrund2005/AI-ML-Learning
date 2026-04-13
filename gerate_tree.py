import os

def print_tree(directory, prefix=''):
    # Folders to ignore so your README stays clean
    ignore = {'.git', '__pycache__', '.ipynb_checkpoints'}
    
    entries = sorted([e for e in os.listdir(directory) if e not in ignore])
    for i, entry in enumerate(entries):
        path = os.path.join(directory, entry)
        is_last = (i == len(entries) - 1)
        connector = '└── ' if is_last else '├── '
        print(prefix + connector + entry)
        
        if os.path.isdir(path):
            extension = '    ' if is_last else '│   '
            print_tree(path, prefix + extension)

if __name__ == '__main__':
    print('```text')
    print('AI-ML-Learning/')
    print_tree('.')
    print('```')