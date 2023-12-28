import os

base = r'C:\Users\idavi\Music\iTunes\iTunes Media\Music'
lookfor = ('A','B')

if __name__ == "__main__":
    dirs = os.listdir(base)
    for dir in dirs:
        if dir.upper().startswith(lookfor):
            print(dir)
    # for (root, dirs) in os.walk(base, topdown=True):
    #     for dir in dirs:
    #         print(os.path.join(root, dir))