
import os

sep = '--'
directories = set()
for dir_name in os.listdir('/data/media/0/realdata'):
  try:
    split_dir_name = dir_name.split(sep)
    directories.add(sep.join(dir_name.split(sep)[:-1]))
  except:
    pass

r = Route(sorted(directories)[-1])
print(r.name.canonical_name)
print(f'segments: 0-{len(r.segments) - 1}')

