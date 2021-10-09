from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

print("starting")
observer = Observer()
fs_change_handler = FileSystemEventHandler()
observer.schedule(fs_change_handler, "/bin", recursive=True)
observer.start()
observer.join()
print("done")
